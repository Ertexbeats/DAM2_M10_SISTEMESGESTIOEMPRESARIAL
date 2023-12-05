from proven.shopping.model.Product import Product
from proven.shopping.model.persist.Dbconnect import Dbconnect


class Shop:

    def __init__(self):
        self.products = []
        self.productsCart = []
        # self.initProducts()
        self.db = Dbconnect()
        self.connection, self.cursor = self.db.dbConnection()
        self.initProducts()

    def initProducts(self):

        self.products = self.fetsh_data()

    def fetsh_data(self):
        try:
            if self.connection and self.cursor:
                self.cursor.execute("SELECT * FROM productos")
                rows = self.cursor.fetchall()
                products = []
                if rows:
                    for row in rows:
                        product = Product(row[0], row[1], row[2], row[3], row[4])
                        products.append(product)
                    return products
                else:
                    print("No products available")
                    return []
        except Exception as e:
            print("Error:", e)
            return []
        finally:
            try:
                if hasattr(self, 'cursor') and self.cursor:
                    self.cursor.close()
                if hasattr(self, 'connection') and self.connection:
                    self.connection.close()
            except Exception as e:
                print("Error closing connection:", e)
