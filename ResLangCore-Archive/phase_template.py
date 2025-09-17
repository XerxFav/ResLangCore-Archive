# phase_template.py — базовый шаблон фазовой структуры

class PhaseTemplate:
    def __init__(self, name, transitions):
        self.name = name
        self.transitions = transitions

    def is_valid_transition(self, target_phase):
        return target_phase in self.transitions

# Пример использования
if __name__ == "__main__":
    neutral_phase = PhaseTemplate("neutral", ["positive", "negative"])
    print(neutral_phase.is_valid_transition("positive"))  # True
