# scanner/target_manager.py

class TargetManager:
    def __init__(self):
        self.targets = []

    def add_target(self, url):
        self.targets.append(url)

    def get_targets(self):
        return self.targets
