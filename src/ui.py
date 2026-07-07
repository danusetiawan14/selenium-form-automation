from src.banner import show_banner


def show_startup(customers):
    """
    Menampilkan banner dan informasi awal aplikasi.
    """

    show_banner()

    print("📥 Reading Excel file...")
    print(f"✅ Customers loaded : {len(customers)}")

    print()
    print("══════════════════════════════════════════════════════════════")
    print()


def show_browser_start():
    """
    Informasi browser mulai dijalankan.
    """

    print("🚀 Starting browser...")
    print()


def show_summary(results):
    """
    Menampilkan ringkasan hasil automation.
    """

    success = sum(
        1 for r in results if r["status"] == "Success"
    )

    failed = sum(
        1 for r in results if r["status"] == "Failed"
    )

    print()
    print("══════════════════════════════════════════════════════════════")
    print()

    print("📊 EXECUTION SUMMARY")
    print()

    print(f"✔ Success        : {success}")
    print(f"✖ Failed         : {failed}")
    print(f"📸 Screenshots   : {success}")
    print("📄 Excel Report  : data/output.xlsx")
    print("📝 Log File      : logs/automation.log")

    print()
    print("══════════════════════════════════════════════════════════════")
    print()

    print("🎉 Automation completed successfully!")
    print()