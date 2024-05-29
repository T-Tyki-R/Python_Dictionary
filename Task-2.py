# Advanced Data Handling w/ Python

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

hotel_rooms["103"] = {"status": "booked", "customer": "Bobby Brown"}

for i, x in hotel_rooms.items():
    for y in x:
        if y == "status":
           x[y] = "available"
        if y == "customer":
               x[y] = ""
        
print(hotel_rooms)

            
for i, x in hotel_rooms.items():
    for y in x:
        if y == "status":
            print(f"Room {i}'s {y}: {x[y]}")