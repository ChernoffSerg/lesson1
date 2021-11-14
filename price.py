def discounted(price, discount, max_discount=20):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)

# product = {'name': 'Samsung Galaxy S21', 'price': 50000.0, 'discount': 5}
# product['price_discounted'] = discounted(product['price'], product['discount'])
# print(product)

#print(discounted(100, 50, max_discount=60))

print(discounted(100, 50, max_discount=50))