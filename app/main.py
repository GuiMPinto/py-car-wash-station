class Car:
    def __init__(self, comfort_class: int, clean_mark :int, brand: str):
            self.comfort_class = comfort_class
            self.clean_mark = clean_mark
            self.brand = brand

class CarWashStation:
    def __init__(self, distance_from_city_center: int, clean_power :int, average_rating: int, count_of_ratings: int):
            self.distance_from_city_center = distance_from_city_center
            self.clean_power = clean_power
            self.average_rating = average_rating
            self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        total_price = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                car.clean_mark = self.clean_power
                total_price += round((car.comfort_class * (self.clean_power - car.clean_mark) * (self.average_rating / self.distance_from_city_center)), 1)
        return total_price

    def calculate_washing_price(self, car: Car) -> float:
        total_price = 0
        total_price += round((car.comfort_class * (self.clean_power - car.clean_mark) * (self.average_rating / self.distance_from_city_center)), 1)
        return total_price

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, nota: int) -> None:
            self.count_of_ratings += 1
            self.average_rating = ((self.average_rating * (self.count_of_ratings - 1)) + nota) / self.count_of_ratings
