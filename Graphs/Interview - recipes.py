'''
 You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.
 You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.
 Return a list of all the recipes that you can create. You may return the answer in any order.

Example
Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
Output: ["bread"]

Example:
 Input: recipes = ["bread","sandwich"],
 ingredients = [["yeast","flour"],["bread","meat"]],
 supplies = ["yeast","flour","meat"]
 Output: ["bread","sandwich"]

 Input: recipes = ["bread", "pancakes","sandwich"],
 ingredients = [["yeast","flour"],[bread, eggs],["bread","meat"]],
 supplies = ["yeast","flour","meat"]
 Output: ["bread","sandwich"]
'''
#This works, but looks like this should be done in topological sort - every one else is doing it that way.

# Time complexity = O(r + (i * s))

def can_receipe_be_made(recipes, ingredients, supplies):
    # Revisit
    visited = {}
    result = []

    def can_be_made(node):
        recipe = recipes[node]

        if recipe in visited:
            return visited[recipe]

        visited[recipe] = False

        for ing in ingredients[node]:
            if ing in supplies:
                continue

            if ing in recipes:
                can_make = can_be_made(recipes.index(ing))
                if not can_make:
                    visited[recipe] = False
                    return False
            else:
                visited[recipe] = False
                return False

        visited[recipe] = True
        return True

    for i, recipe in enumerate(recipes):
        if can_be_made(i):
            result.append(recipe)

    return result


# print(can_receipe_be_made(recipes=["bread"], ingredients=[["yeast", "flour"]], supplies=["yeast", "flour", "corn"]) == [
#     'bread'])
#
# print(can_receipe_be_made(recipes=["bread", "sandwich"],
#                           ingredients=[["yeast", "flour"], ["bread", "meat"]],
#                           supplies=["yeast", "flour", "meat"]) == ['bread', 'sandwich'])
#
# print(can_receipe_be_made(recipes=["bread", "sandwich", "pancakes"],
#                           ingredients=[["yeast", "flour"], ["bread", "meat"], ["eggs", "vanilla"]],
#                           supplies=["yeast", "flour", "meat"]) == ['bread', 'sandwich'])

print(can_receipe_be_made(recipes=["bread", "sandwich"],
                          ingredients=[["sandwich"], ["bread", "yeast"]],
                          supplies = ["yeast"]) == [])

print(can_receipe_be_made(recipes=["bread", "sandwich", "pancakes", "batter"],
                          ingredients=[["yeast", "flour"], ["bread", "meat"], ["batter"], ["pancakes"]],
                          supplies=["yeast", "flour", "meat"]) == ['bread', 'sandwich'])

# print(can_receipe_be_made(recipes = ["ju","fzjnm","x","e","zpmcz","h","q"],
#                           ingredients = [["d"],["hveml","f","cpivl"],["cpivl","zpmcz","h","e","fzjnm","ju"],["cpivl","hveml","zpmcz","ju","h"],["h","fzjnm","e","q","x"],["d","hveml","cpivl","q","zpmcz","ju","e","x"],["f","hveml","cpivl"]],
#                           supplies = ["f","hveml","cpivl","d"]))