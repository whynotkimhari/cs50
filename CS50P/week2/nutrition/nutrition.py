fruits = ["apple", "avocado", "banana", "cantaloupe", "grapefruit", "grapes", "honeydew melon", "kiwifruit", "lemon", "lime", "nectarine", "orange","peach","pear","pinenapple", "plums", "strawberries", "sweet cherries", "tangerine", "watermelone"]
calories = [130, 50, 110, 50, 60, 90, 50, 90 , 15, 20, 60 , 80, 60, 100,50,70,50,100,50,80]
fruit_input = input("Item: ").lower().strip()

for i in range(len(fruits)):
    if fruits[i] == fruit_input:
        print("Calories:",calories[i])