class PaperTray:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.paper_count = 0

    def load_paper(self, count):
        if self.paper_count + count <= self.capacity:
            self.paper_count += count
            print(f"Loaded {count} sheets of paper. Current paper count: {self.paper_count}/{self.capacity}")
        else:
            print(f"Paper tray is full. Cannot load more paper.")

    def use_paper(self, count):
        if self.paper_count >= count:
            self.paper_count -= count
            print(f"Used {count} sheets of paper. Current paper count: {self.paper_count}/{self.capacity}")
        else:
            print("Not enough paper in the tray to print.")