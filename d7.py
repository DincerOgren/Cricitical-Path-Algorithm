tasks = {}

while True:
    try:
        num_tasks = int(input("Kaç tane görev var? "))
        if num_tasks < 0:
            print("Görev sayısı negatif olamaz. Lütfen pozitif bir sayı girin.")
            continue
        break
    except ValueError:
        print("Görev sayısı bir sayı olmalıdır. Lütfen sayı girin.")

for i in range(num_tasks):
    while True:
        task = input("Görevin adı nedir? ")
        if task in tasks:
            print("Bu görev zaten var. Lütfen farklı bir görev adı girin.")
            continue
        break

    while True:
        try:
            duration = int(input("Görevin süresi kaç gün? "))
            if duration < 0:
                print("Görev süresi negatif olamaz. Lütfen pozitif bir sayı girin.")
                continue
            break
        except ValueError:
            print("Görev süresi bir sayı olmalıdır. Lütfen sayı girin.")
    tasks[task] = duration

    while True:
        update_input = input("Görevin süresini değiştirmek ister misiniz? [E/H] ").lower()
        if update_input == "e":
            while True:
                try:
                    duration = int(input("Yeni görevin süresi kaç gün? "))
                    if duration < 0:
                        print("Görev süresi negatif olamaz. Lütfen pozitif bir sayı girin.")
                        continue
                    break
                except ValueError:
                    print("Görev süresi bir sayı olmalıdır. Lütfen sayı girin.")
            tasks[task] = duration
            break
        elif update_input == "h":
            break
        else:
            print("Lütfen 'E' veya 'H' girin.")

dependencies = {}
for task in tasks:
    while True:
        depends_on = input(f"{task} görevi hangi görevlere bağlı? (Virgülle ayrılmış) ")
        if depends_on:
            depends_on = depends_on.split(",")
            invalid_dependencies = [dep for dep in depends_on if dep not in tasks]
            if invalid_dependencies:
                print(f"{', '.join(invalid_dependencies)} adında görevler yok. Lütfen geçerli görev adlarını girin.")
                continue
        else:
            depends_on = []
        break
    if depends_on:
        dependencies[task] = depends_on

for task, depends_on in dependencies.items():
    for dep in depends_on:
        if dep not in tasks:
            print(f"{dep} adında bir görev yok. Lütfen geçerli bir görev adı girin.")
            del dependencies[task]
            break

end_times = {task: 0 for task in tasks}
for task in tasks:
    depends_on = dependencies.get(task, [])
    if depends_on:
        dependency_end_times = [end_times[dep] for dep in depends_on]
    else:
        dependency_end_times = []
    if dependency_end_times:
        end_time = max(dependency_end_times) + tasks[task]
    else:
        end_time = tasks[task]
    end_times[task] = end_time

project_duration = max(end_times.values())
print(f"Proje {project_duration} gün sürecek.")
