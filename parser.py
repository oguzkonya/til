import os

folders = os.listdir()
folders.sort()

categories = {
    "android": "Android",
    "csharp": "C#",
    "git": "Git",
    "maths": "Maths",
    "netflix": "Netflix"
}

readme = "# TIL: Today I Learned\n\n"
readme += "A personal knowledge base. Not necessarily today, but these are the things I learned that are too short to be a full blog post.\n"

for folder in folders:
    if os.path.isdir(folder) and not folder.startswith("."):
        files = os.listdir(folder)

        readme += "\n### %s\n\n" % categories[folder]

        for f in files:
            if not f.startswith("."):
                path = "./%s/%s" % (folder, f)

                with open(path) as ff:

                    print(path)
                    r = ff.readline()
                    print(r)
                    firstLine = r.strip().replace("# ", "")
                    line = "- [%s](%s/%s)\n" % (firstLine, folder, f)
                    readme += line

with open("README.md", "w") as r:
    r.write(readme)
    r.close()