from django.shortcuts import render, redirect
from .forms import PDFUploadForm
import PyPDF2
import os
def home(request):
    return render(request,"index.html")

# def upload(request):
#     return render(request,"getcv.html")



def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print("valid")
            uploaded_pdf = form.save()
            # Extract text from the uploaded PDF
            pdf_text = extract_text_from_pdf(uploaded_pdf.pdf_file)
            # Delete the uploaded PDF file
            delete_uploaded_pdf(uploaded_pdf.pdf_file.path)
            # Redirect to display the extracted text
            skills=[]
            for i in range(0,len(programming_languages)):
                if programming_languages[i].lower() in pdf_text.lower():
                    skills.append(programming_languages[i])
            print(skills)
            return result(request, pdf_text=skills)
    else:
        print("invalid")

        form = PDFUploadForm()
    return render(request, 'getcv.html', {'form': form})
def extract_text_from_pdf(pdf_file):
    pdf_text = ''
    try:
        # Get the file path from the FieldFile object
        pdf_file_path = pdf_file.path
        with open(pdf_file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            for page_number in range(num_pages):
                page = reader.pages[page_number]
                pdf_text += page.extract_text()
    except Exception as e:
        print("Error extracting text from PDF:", e)



    return pdf_text

def delete_uploaded_pdf(pdf_path):
    try:
        if os.path.exists(pdf_path):
            os.remove(pdf_path)
    except Exception as e:
        print("Error deleting PDF:", e)

def result(request, pdf_text):
    return render(request, 'result.html', {'Skills': pdf_text})
programming_languages = [
    "HTML",
    "CSS",
    "JavaScript",
    "TypeScript",
    "React",
    "Angular",
    "Vue.js",
    "Sass",
    "Less",
    "Bootstrap",
    "Tailwind CSS",
    "Material-UI",
    "Bulma",
    "Foundation",
    "Semantic UI",
    "Ant Design",
    "UIKit",

    "Gatsby",
    "Next.js",
    "Nuxt.js",
    "Node.js",
    "Python",
    "Ruby",
    "Java",
    "PHP",
    "Go",
    "C#",
    "Express.js",
    "Django",
    "Flask",
    "Ruby on Rails",
    ".NET",
    "Spring",
    "Laravel",
    "Symfony",
    "ASP.NET",
    "Gin", "MySQL",
    "PostgreSQL",
    "SQLite",
    "MongoDB",
    "Microsoft SQL Server",
    "Oracle",

    "Redis",
    "Couchbase",
    "Cassandra",
    "DynamoDB",
    "MariaDB",
    "Neo4j",
    "Elasticsearch",
    "Amazon RDS",

    "Supabase",
    "Git",
    "GitHub",
    "GitLab",
    "Bitbucket",
    "Jira",
    "Trello",
    "Slack",
    "VS Code",
    "Sublime Text",
    "Atom",
    "IntelliJ IDEA",
    "Eclipse",
    "Visual Studio",
    "Postman",
    "Docker",
    "Kubernetes",
    "Jenkins",
    "Travis CI",
    "CircleCI",
    "TeamCity",
    "Splunk",
    "New Relic","CPU",
    "GPU",
    "RAM",
    "SSD",
    "HDD",
    "Motherboard",
    "Power Supply Unit (PSU)",
    "Graphics Card",
    "Network Interface Card (NIC)",
    "Router",
    "Switch",
    "Server",
    "Microcontroller",
    "Arduino",
    "Raspberry Pi",
    "Sensors",
    "Wearable Devices",
    "Virtual Reality (VR) Headsets",
    "Augmented Reality (AR) Devices",
"Router",
    "Switch",
    "Firewall",
    "Load Balancer",
    "Wireless Access Point (WAP)",
    "Ethernet",
    "TCP/IP",
    "DNS",
    "DHCP",
    "VPN",
    "SSL/TLS",
    "BGP (Border Gateway Protocol)",
    "OSPF (Open Shortest Path First)",
    "Spanning Tree Protocol (STP)",
    "VLAN (Virtual LAN)",
    "Subnetting",
    "CIDR (Classless Inter-Domain Routing)",
    "IPv4",
    "IPv6",
    "Network Security",
    "Network Monitoring Tools",
    "Packet Sniffers",
    "Wireshark",
    "Kotlin",
    "Android Studio",
    "XML",
    "Activities",
    "Fragments",
    "Intents",
    "RecyclerView",
    "Adapters",
    "SQLite",
    "JSON",
    "RESTful APIs",

    "Material Design",
    "Android SDK",
    "Gradle",
    "Android NDK",
    "Jetpack Compose",
    "Android Architecture Components",
    "Google Play Store",
    "Android Emulator",
    "Flutter",
    "React Native",
    "Swift",
    "Objective-C",
    "Xcode",
    "Interface Builder",
    "UIKit",
    "SwiftUI",
    "Auto Layout",
    "Core Data",
    "Cocoa Touch",
    "RESTful APIs",
    "JSON",
    "Firebase",
    "TestFlight",
    "Apple Developer Account",
    "App Store Connect",
    "iOS Simulator",
    "In-App Purchases",
    "Push Notifications",
    "ARKit",
    "Core ML",
    "C#",
    "C++",
    "Electron",
    "Qt",
    "Windows Forms",
    "WPF (Windows Presentation Foundation)",
    "GTK (GIMP Toolkit)",
    "Swing",
    "JavaFX",
    "Cocoa (macOS)",
    "Win32 API",
    "GTK#",
    "Avalonia",
    "PyQt",
    "Tkinter",
    "wxWidgets",
    "Universal Windows Platform (UWP)",

]
