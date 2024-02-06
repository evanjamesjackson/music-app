from lastipy.flows.new_releases import save_new_releases

if __name__ == "__main__":
    save_new_releases.serve(
        name="new_releases_deployment", 
        cron="* * * * *"
    )