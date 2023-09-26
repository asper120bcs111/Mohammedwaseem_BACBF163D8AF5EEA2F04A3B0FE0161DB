#Write a function called linear_search_product that takes the list of products and a target product name as input. The function should perform a linear search to find the target product in the list and return a list of indices of all occurrences of the product if found, or an empty list if the product is not found
def linear_search_product(products, target_product):
    indices = []
    for index, product in enumerate(products):
        if product == target_product:
            indices.append(index)
    return indices



# Sample list of products
product_list = ["apple", "banana", "orange", "apple", "grape", "apple"]

# Target product to search for
target_product = "apple"

# Call the function
result = linear_search_product(product_list, target_product)

# Print the result
print(result)