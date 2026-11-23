# ============================================
# আমার কাজের তালিকা (To-Do List)
# একজন নতুন প্রোগ্রামারের প্রথম পাইথন প্রজেক্ট
# ============================================

tasks = []  # সব কাজ এখানে জমা থাকবে (একটা লিস্ট/তালিকা)


def show_menu():
    print("\n===== মেনু =====")
    print("1. নতুন কাজ যোগ করুন")
    print("2. সব কাজ দেখুন")
    print("3. কাজ সম্পন্ন হিসেবে মার্ক করুন")
    print("4. কাজ মুছে ফেলুন")
    print("5. বের হয়ে যান")


def add_task():
    task_name = input("কোন কাজ যোগ করতে চান? ")
    tasks.append({"name": task_name, "done": False})
    print(f'"{task_name}" যোগ করা হয়েছে!')


def show_tasks():
    if not tasks:
        print("তালিকায় এখনো কোনো কাজ নেই।")
        return

    print("\n--- আপনার কাজের তালিকা ---")
    for index, task in enumerate(tasks, start=1):
        status = "✅ সম্পন্ন" if task["done"] else "⏳ বাকি আছে"
        print(f'{index}. {task["name"]} - {status}')


def complete_task():
    show_tasks()
    if not tasks:
        return
    try:
        number = int(input("কোন নম্বরের কাজ সম্পন্ন হয়েছে? "))
        tasks[number - 1]["done"] = True
        print("দারুণ! কাজটি সম্পন্ন হিসেবে চিহ্নিত হলো।")
    except (ValueError, IndexError):
        print("সঠিক নম্বর দিন।")


def delete_task():
    show_tasks()
    if not tasks:
        return
    try:
        number = int(input("কোন নম্বরের কাজ মুছতে চান? "))
        removed = tasks.pop(number - 1)
        print(f'"{removed["name"]}" মুছে ফেলা হয়েছে।')
    except (ValueError, IndexError):
        print("সঠিক নম্বর দিন।")


def main():
    print("আপনার কাজের তালিকায় স্বাগতম!")
    while True:
        show_menu()
        choice = input("আপনার পছন্দ লিখুন (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("ধন্যবাদ! আবার আসবেন।")
            break
        else:
            print("ভুল পছন্দ, আবার চেষ্টা করুন।")


if __name__ == "__main__":
    main()
