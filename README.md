# Love Me Some Ice Cream

This is a website that allows users to search ice cream data from the database. This website is built by Flask framework with the help of bootstrap in the front end. Querying database uses all SQL. A detailed writeup can be found [here](https://petertu.gatsbyjs.io/blog/love-me-some-ice-cream).

## Details

- Team members: [Helen Du](https://github.com/helenduz), [Yucheng Yang](https://github.com/YuchengY), Peter Tu
- Starting webpage: index.html

## Known bugs:

Using browser back button when returning from `product_list(product_list.html)` to home page(index.html) and hit search button again will return all products (the search filter will not work even though the conditions put in before will be there).
