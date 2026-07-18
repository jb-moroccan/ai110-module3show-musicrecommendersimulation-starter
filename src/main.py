"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""
#from recommender import load_songs, recommend_songs

from pathlib import Path

try:
    from src.recommender import load_songs, recommend_songs
except ImportError:
    from recommender import load_songs, recommend_songs


def main() -> None:
    #songs = load_songs("data/songs.csv")
    project_root = Path(__file__).resolve().parent.parent
    songs_path = project_root / "data" / "songs.csv"
    songs = load_songs(str(songs_path))
    print(f"Loaded songs: {len(songs)}")

    # Three distinct taste profiles to compare different recommendation styles
    user_profiles = [
        {
            "name": "High Energy Pop",
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.8,
            "likes_acoustic": False,
        },
        {
            "name": "Deep Intense Rock",
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 0.9,
            "likes_acoustic": False,
        },
        {
            "name": "Chill Lofi",
            "favorite_genre": "lofi",
            "favorite_mood": "chill",
            "target_energy": 0.4,
            "likes_acoustic": True,
        },
    ]

    for user_prefs in user_profiles:
        print(f"\nProfile: {user_prefs['name']}\n")
        recommendations = recommend_songs(user_prefs, songs, k=3)
        for rec in recommendations:
            song, score, explanation = rec
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
