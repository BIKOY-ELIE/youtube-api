from classes.VideoSave import save_video
from classes.VideoFetcher import VideoFetcher
from classes.VideoFormat import VideoFormat
from classes.NextPageTokenWrite import NextPageTokenWrite
import os
from classes.GoogleAPIConnection import GoogleAPIConnection
import googleapiclient.errors


vds = VideoFetcher()
vd_fmt = VideoFormat()

keys_list = [os.getenv("API_KEY"), os.getenv("API_KEY1"), os.getenv(
    "API_KEY2"), os.getenv("API_KEY3")]

list_domains = ["bootstrap", "material ui", "SCSS", "SDL C", "Sass", "Java EE", "game development", "py2neo", "nextjs", "getting started in Nodejs express js", "nodejs adonis", "Ruby on rails", "angular js", "vanilla js", "javafx", "javaswing", "turtle python", "getting started in xml", "devsecops", "fxml", "flask python", ".NET framework", "Unity", "qt", "QML", "Gsap javacript" "cypher neo4j", "PostgreSql", "AuraDB", "datascience", "artificiel Intelligence", "machine learning", "ethical hacking", "cybersecurity", "deep learning", "flask python", ".NET framework", "Unity", "qt", "QML", "Gsap javacript", "frontend", "backend","introduction in programming", "react", "vuejs", "CSS", "HTML", "JavaScript", "Java", "Python", "PHP", "ruby", "C++", "C", "C#", "Kotlin", "dart", "Scala", "GO", "getting started in FrontEnd", "getting started in BackEnd", "MySQL", "SQLite", "neo4j", "firebase", "Fast API", "HuggingFace", "Kubernetes", "Docker", "DevOPs", "SCRUM methodologie", "tailwind css", "web programming", "Mobile programming", "NoSQL database","Django python", "Pygame python", "Py2neo", "JavaFx", "NoSQL", "SQL", "Jquery", "nuxtjs"]

for key in keys_list:
    i = 0
    try:
        GAC = GoogleAPIConnection()
        txt = NextPageTokenWrite()
        for domain in list_domains:
            print(f"{domain} \n\n")
            videos = vds.fetch_videos(domain, GAC.connection(key))
            print(len(videos))
            print('\n\n')
            print(f" \n\n\{domain} \n\n")
            txt.write_last_domain(domain)
            if len(videos) > 0: i = i + 1
        break
    except googleapiclient.errors.HttpError:
        pass
    finally:
        del list_domains[0:i+1]