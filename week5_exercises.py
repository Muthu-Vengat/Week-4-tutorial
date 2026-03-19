movies = {
    "Dune": 12.5,
    "Barbie": 11.0,
    "Oppenheimer": 13.0,
    "Spirited Away": 10.0
}

purchases = []

while True:
  movie_name = input("Which movie would you like to watch ")
  if movie_name == "done":
    break
  if movie_name not in movies:
    print(movies)
    continue

  qty = int(input("How many tickets would you like: "))
  purchases.append(qty)
  print("Receipt")
  price = movies[movie_name]
  It = qty * price
  print(It)

