def sandwich(*food_material):
    print("你要加的食材有: ")
    for food in food_material:
        print("-" + food)
sandwich('沙拉', '牛肉', '鸡肉')
sandwich('沙拉')
sandwich('牛肉', '鸡肉')