from fastapi import APIRouter, Request, HTTPException

router = APIRouter()

@router.get("/users_rated", response_description="List users who rated a movie")
def list_users_rated_movie(request: Request, movie_name: str):
    session = request.app.neo4j_driver.session(database="movies")
    try:
        query = """
        MATCH (p:Person)-[r:REVIEWED]->(m:Movie)
        WHERE m.title = $movie_name
        RETURN p.name AS user_name, r.rating AS rating
        """
        result = session.run(query, movie_name=movie_name)
        users = [{"user_name": record["user_name"], "rating": record["rating"]} for record in result]
        return users
    finally:
        session.close()

@router.get("/user_ratings", response_description="Get a user with the number of movies they have rated and the list of rated movies")
def get_user_ratings(request: Request, user_name: str):
    session = request.app.neo4j_driver.session(database="movies")
    try:
        query = """
        MATCH (p:Person)-[r:REVIEWED]->(m:Movie)
        WHERE p.name = $user_name
        RETURN p.name as userName, count(m) as numberOfRatedMovies, collect(m.title) as ratedMovies
        """
        result = session.run(query, user_name=user_name)
        user_data = result.single()
        if not user_data:
            raise HTTPException(status_code=404, detail=f"User with name {user_name} not found")
        return {
            "user_name": user_data["userName"],
            "movie_count": user_data["numberOfRatedMovies"],
            "rated_movies": user_data["ratedMovies"]
        }
    finally:
        session.close()