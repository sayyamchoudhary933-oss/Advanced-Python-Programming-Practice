from datetime import datetime


# Decorator to add a border around the report
def add_border(func):
    def wrapper(self):
        report = func(self)
        line = "=" * 60
        return f"{line}\n{report}\n{line}"
    return wrapper


# Decorator to add the current date
def add_date(func):
    def wrapper(self):
        report = func(self)
        date = datetime.now().strftime("%Y-%m-%d")
        return f"Date: {date}\n{report}"
    return wrapper


class Report:
    templates = {}

    def __init__(self, title, data):
        self.title = title
        self.data = data

    @classmethod
    def add_template(cls, name, title):
        cls.templates[name] = title
        print(f"Template '{name}' added successfully.")

    @classmethod
    def create_from_template(cls, template_name, data):
        if template_name not in cls.templates:
            raise ValueError("Template not found.")

        return cls(cls.templates[template_name], data)

    def generate(self):
        result = f"\n{self.title}\n"

        for key, value in self.data.items():
            result += f"{key}: {value}\n"

        return result

    def __str__(self):
        return self.generate()

    def __len__(self):
        return len(self.data)


class FormattedReport(Report):

    @add_border
    def generate(self):
        return super().generate()


class DatedReport(Report):

    @add_date
    def generate(self):
        return super().generate()


class ProfessionalReport(Report):

    @add_border
    @add_date
    def generate(self):
        return super().generate()


def get_report_data():
    data = {}

    print("\nEnter report fields.")
    print("Type 'done' as the field name when finished.")

    while True:
        key = input("Enter field name: ").strip()

        if key.lower() == "done":
            break

        if not key:
            print("Field name cannot be empty.")
            continue

        value = input(f"Enter value for '{key}': ")
        data[key] = value

    return data


def main():
    print("========== DYNAMIC REPORT GENERATOR ==========")

    # Add default templates
    Report.templates = {
        "student": "Student Performance Report",
        "sales": "Sales Report",
        "employee": "Employee Report"
    }

    while True:
        print("\n========== MENU ==========")
        print("1. Add Report Template")
        print("2. Generate Basic Report")
        print("3. Generate Bordered Report")
        print("4. Generate Dated Report")
        print("5. Generate Professional Report")
        print("6. Display Templates")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter template name: ").strip()
            title = input("Enter report title: ").strip()

            if not name or not title:
                print("Template name and title cannot be empty.")
            else:
                Report.add_template(name, title)

        elif choice in ["2", "3", "4", "5"]:
            if not Report.templates:
                print("No templates available.")
                continue

            print("\nAvailable Templates:")
            for name in Report.templates:
                print("-", name)

            template_name = input("Enter template name: ").strip()

            if template_name not in Report.templates:
                print("Template not found.")
                continue

            data = get_report_data()

            if choice == "2":
                report = Report.create_from_template(template_name, data)
            elif choice == "3":
                base_report = Report.create_from_template(template_name, data)
                report = FormattedReport(base_report.title, base_report.data)
            elif choice == "4":
                base_report = Report.create_from_template(template_name, data)
                report = DatedReport(base_report.title, base_report.data)
            else:
                base_report = Report.create_from_template(template_name, data)
                report = ProfessionalReport(base_report.title, base_report.data)

            print("\nGenerated Report:")
            print(report)
            print(f"Number of fields: {len(report)}")

        elif choice == "6":
            print("\nAvailable Templates:")
            for name, title in Report.templates.items():
                print(f"{name} -> {title}")

        elif choice == "7":
            print("Thank you for using the Dynamic Report Generator!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
