import random
import json

import os

# Define data storage file
progress_file = "progress.json"

def load_progress():
    if os.path.exists(progress_file):
        with open(progress_file, "r") as file:
            return json.load(file)
    return {}

def save_progress(progress):
    with open(progress_file, "w") as file:
        json.dump(progress, file)

# Function to ask a question and return if the answer was correct
from typing import Dict, Any, List

def load_questions() -> List[Dict[str, Any]]:
    with open("questions.json", "r") as file:
        return json.load(file)
def ask_question(question: Dict[str, Any]) -> bool:
    if question['type'] == 'multiple_choice':
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i + 1}. {option}")
        try:
            answer_index = int(input("Enter the number of your answer: ")) - 1
            answer = question['options'][answer_index]
        except (ValueError, IndexError):
            print("Invalid choice.")
            return False
        return answer == question['answer']
    elif question['type'] == 'true_false':
        print(question['question'])
        answer = input("Enter True or False: ").strip().lower() == 'true'
        return answer == question['answer']
    elif question['type'] == 'scenario':
        print(question['question'])
        input("Press Enter to see the answer...")
        print(question['answer'])
        return True

def quiz(questions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    incorrect_answers = []
    for question in questions:
        if not ask_question(question):
            incorrect_answers.append(question)
    return incorrect_answers

def review_incorrect(incorrect_answers: List[Dict[str, Any]]):
    if not incorrect_answers:
        print("No incorrect answers to review.")
        return
    print("\nReview of Incorrect Answers:")
    for question in incorrect_answers:
        print(f"\nQuestion: {question['question']}")
        if question['type'] == 'multiple_choice':
            print(f"Options: {', '.join(question['options'])}")
        print(f"Correct Answer: {question['answer']}")
        if question['type'] == 'scenario':
            print(f"Explanation: {question['answer']}")

def select_questions(questions: Dict[str, Any], num_questions: int, selected_domains: List[str]) -> List[Dict[str, Any]]:
    selected_questions = []
    for domain in selected_domains:
        domain_questions = questions.get(domain, [])
        if len(domain_questions) > 0:
            selected_questions.extend(random.sample(domain_questions, min(num_questions, len(domain_questions))))
    return selected_questions

def show_progress():
    progress = load_progress()
    for domain, count in progress.items():
        print(f"{domain}: {count} questions answered correctly")

def select_domains() -> List[str]:
    print("Available domains:")
    for i, domain in enumerate(questions.keys()):
        print(f"{i + 1}. {domain}")
    choices = input("Select domains (comma-separated numbers): ").split(',')
    selected_domains = [list(questions.keys())[int(choice.strip()) - 1] for choice in choices]
    return selected_domains

questions = {
    "1.0 General Security Concepts": [
        {
            "type": "multiple_choice",
            "question": "Which of the following is NOT a type of security control?",
            "options": ["Preventive", "Detective", "Corrective", "Destructive"],
            "answer": "Destructive",
            "objective": "1.1 Compare and contrast various types of security controls"
        },
        {
            "type": "true_false",
            "question": "Data masking involves altering data to protect sensitive information.",
            "answer": True,
            "objective": "1.3 Explain the importance of data protection and privacy"
        },
        {
            "type": "true_false",
            "question": "Non-repudiation ensures that a user cannot deny having performed an action.",
            "answer": True,
            "objective": "1.2 Summarize fundamental security concepts"
        },
      {
            "type": "multiple_choice",
            "question": "Which term refers to a method of ensuring data integrity by generating a unique value for data?",
            "options": ["Hashing", "Encryption", "Tokenization", "Steganography"],
            "answer": "Hashing",
            "objective": "1.1 Compare and contrast various types of security controls"
        },
        {
            "type": "multiple_choice",
            "question": "Which of the following is NOT a typical use of steganography?",
            "options": ["Hiding messages in images", "Watermarking documents", "Encrypting network traffic", "Concealing data in audio files"],
            "answer": "Encrypting network traffic",
            "objective": "1.4 Explain the importance of using appropriate cryptographic solutions"
        },
        {
            "type": "true_false",
            "question": "Full-disk encryption protects data when the device is powered off but not when it's running.",
            "answer": True,
            "objective": "1.4 Explain the importance of using appropriate cryptographic solutions"
        },
         {
            "type": "multiple_choice",
            "question": "Which of the following is an example of a preventive control?",
            "options": ["Firewalls", "Intrusion Detection Systems", "Security Incident Response", "Audit Logs"],
            "answer": "Firewalls",
            "objective": "1.1 Compare and contrast various types of security controls"
        },
    ],
    "2.0 Threats, Vulnerabilities, and Mitigations": [
        {
            "type": "multiple_choice",
            "question": "Which threat actor is most likely to be motivated by financial gain?",
            "options": ["Hacktivist", "Script kiddie", "Organized crime", "Nation-state"],
            "answer": "Organized crime",
            "objective": "2.1 Compare and contrast common threat actors and motivations"
        },
        {
            "type": "true_false",
            "question": "Phishing attacks are always delivered via email.",
            "answer": False,
            "objective": "2.2 Explain common threat vectors and attack surfaces"
        },
        {
            "type": "multiple_choice",
            "question": "What type of malware is designed to disrupt the normal functioning of a system or network?",
            "options": ["Virus", "Worm", "Ransomware", "Adware"],
            "answer": "Ransomware",
            "objective": "2.1 Compare and contrast common threat actors and motivations"
        },
        {
            "type": "true_false",
            "question": "A denial-of-service attack aims to make a system or network resource unavailable to its intended users.",
            "answer": True,
            "objective": "2.2 Explain common threat vectors and attack surfaces"
        },  
        {
            "type": "multiple_choice",
            "question": "Which of the following is NOT a common indicator of malicious activity?",
            "options": ["Unusual outbound network traffic", "Multiple failed login attempts", "Unexpected patching of systems", "Geographical irregularities in access patterns"],
            "answer": "Unexpected patching of systems",
            "objective": "2.4 Given a scenario, analyze indicators of malicious activity"
        },
        {
            "type": "true_false",
            "question": "Implementing the principle of least privilege is an effective mitigation technique against privilege escalation attacks.",
            "answer": True,
            "objective": "2.5 Explain the purpose of mitigation techniques used to secure the enterprise"
        },
        {
            "type": "multiple_choice",
            "question": "Which technique is used to gather information about a target system or network before launching an attack?",
            "options": ["Reconnaissance", "Exploitation", "Scanning", "Social Engineering"],
            "answer": "Reconnaissance",
            "objective": "2.3 Explain various types of vulnerabilities"
        },
        {
            "type": "true_false",
            "question": "Ransomware is designed to steal sensitive data from a victim without their knowledge.",
            "answer": False,
            "objective": "2.1 Compare and contrast common threat actors and motivations"
        }
        
    ],
    "3.0 Security Architecture": [
        {
            "type": "multiple_choice",
            "question": "In a cloud shared responsibility model, which of the following is typically the responsibility of the cloud service provider?",
            "options": ["Data classification", "Network firewalls", "Physical security of data centers", "End-user access management"],
            "answer": "Physical security of data centers",
            "objective": "3.1 Compare and contrast security implications of different architecture models"
        },
        {
            "type": "multiple_choice",
            "question": "What is the main purpose of network segmentation?",
            "options": ["To improve network performance", "To isolate sensitive systems and data", "To increase network speed", "To simplify network management"],
            "answer": "To isolate sensitive systems and data",
            "objective": "3.2 Given a scenario, apply security principles to secure enterprise infrastructure"
        },
        {
            "type": "true_false",
            "question": "Virtual Private Network (VPN) provides encryption for data in transit between the client and the VPN server.",
            "answer": True,
            "objective": "3.3 Apply secure design principles to various technologies"
        },
        {
            "type": "multiple_choice",
            "question": "Which component is commonly used in a DMZ to protect internal resources from external threats?",
            "options": ["Web Application Firewall (WAF)", "Intrusion Prevention System (IPS)", "Network Intrusion Detection System (NIDS)", "Router"],
            "answer": "Web Application Firewall (WAF)",
            "objective": "3.1 Compare and contrast security implications of different architecture models"
        },
        {
            "type": "true_false",
            "question": "Software-defined networking (SDN) always improves network security.",
            "answer": False,
            "objective": "3.2 Given a scenario, apply security principles to secure enterprise infrastructure"
        },
        {
            "type": "scenario",
            "question": "Your organization needs to implement a secure remote access solution for employees. What factors would you consider when choosing between a traditional VPN and a Zero Trust Network Access (ZTNA) solution?",
            "answer": "When choosing between a traditional VPN and ZTNA, consider: 1) Security: ZTNA offers more granular access control and follows the principle of least privilege. 2) User experience: ZTNA can provide seamless access without requiring a VPN client. 3) Scalability: ZTNA is often more scalable for cloud and hybrid environments. 4) Application visibility: ZTNA provides better visibility into application usage. 5) Complexity: Traditional VPNs might be simpler to implement in some cases. 6) Cost: Compare long-term costs of both solutions. 7) Compliance requirements: Ensure the chosen solution meets regulatory standards.",
            "objective": "3.2 Given a scenario, apply security principles to secure enterprise infrastructure"
        },
        {
            "type": "multiple_choice",
            "question": "Which of the following is NOT a common method to secure data at rest?",
            "options": ["Full-disk encryption", "File-level encryption", "Database encryption", "Transport Layer Security (TLS)"],
            "answer": "Transport Layer Security (TLS)",
            "objective": "3.3 Compare and contrast concepts and strategies to protect data"
        },
        {
            "type": "true_false",
            "question": "Hot sites provide the fastest recovery time in a disaster recovery scenario but are typically the most expensive option.",
            "answer": True,
            "objective": "3.4 Explain the importance of resilience and recovery in security architecture"
        },
        {
            "type": "true_false",
            "question": "Data loss prevention (DLP) solutions are primarily designed to monitor and control the flow of sensitive data within an organization.",
            "answer": True,
            "objective": "3.2 Given a scenario, apply security principles to secure enterprise infrastructure"
        }
    ],
    "4.0 Security Operations": [
        {
            "type": "multiple_choice",
            "question": "Which of the following is NOT typically included in a secure baseline configuration?",
            "options": ["Disabling unnecessary services", "Applying latest security patches", "Enabling all network protocols", "Configuring strong password policies"],
            "answer": "Enabling all network protocols",
            "objective": "4.1 Given a scenario, apply common security techniques to computing resources"
        },
        {
            "type": "true_false",
            "question": "Data sanitization always involves the physical destruction of storage media.",
            "answer": False,
            "objective": "4.2 Explain the security implications of proper hardware, software, and data asset management"
        },
        {
            "type": "scenario",
            "question": "Your organization has just completed a vulnerability scan of its network. The scan revealed several critical vulnerabilities. How would you prioritize and address these findings?",
            "answer": "To prioritize and address vulnerability scan findings: 1) Assess the criticality of affected systems and data. 2) Evaluate the CVSS scores of the vulnerabilities. 3) Consider the exploitability and potential impact of each vulnerability. 4) Prioritize vulnerabilities with known exploits in the wild. 5) Create a patching schedule, addressing the most critical vulnerabilities first. 6) Implement compensating controls for vulnerabilities that can't be immediately patched. 7) Retest systems after applying patches to ensure vulnerabilities are resolved. 8) Document all actions taken and update the risk register accordingly.",
            "objective": "4.3 Explain various activities associated with vulnerability management"
        },
        {
            "type": "multiple_choice",
            "question": "Which of the following is NOT a typical feature of a Security Information and Event Management (SIEM) system?",
            "options": ["Log aggregation", "Event correlation", "Intrusion prevention", "Alert generation"],
            "answer": "Intrusion prevention",
            "objective": "4.4 Explain security alerting and monitoring concepts and tools"
        },
        {
            "type": "true_false",
            "question": "Multifactor authentication always requires at least three different authentication factors.",
            "answer": False,
            "objective": "4.5 Given a scenario, implement and maintain identity and access management"
        },
    ],
    "5.0 Security Program Management and Oversight": [
        {
            "type": "multiple_choice",
            "question": "Which of the following is NOT typically included in an organization's security governance structure?",
            "options": ["Security policies", "Risk management framework", "Incident response plan", "Marketing strategy"],
            "answer": "Marketing strategy",
            "objective": "5.1 Summarize elements of effective security governance"
        },
        {
            "type": "true_false",
            "question": "The risk management process is a one-time activity performed at the beginning of a project.",
            "answer": False,
            "objective": "5.2 Explain elements of the risk management process"
        },
        {
            "type": "scenario",
            "question": "Your organization is considering outsourcing its IT help desk to a third-party provider. What steps would you take to assess and manage the risks associated with this decision?",
            "answer": "To assess and manage risks of outsourcing the IT help desk: 1) Conduct a thorough vendor assessment, including their security practices and compliance certifications. 2) Perform a risk assessment to identify potential threats and vulnerabilities introduced by the outsourcing. 3) Review the vendor's incident response and business continuity plans. 4) Ensure the contract includes appropriate security and privacy clauses, including right-to-audit. 5) Implement strong access controls and monitoring for the vendor's access to your systems. 6) Establish clear data handling and privacy requirements. 7) Develop a robust off-boarding process for when the contract ends. 8) Regularly review and audit the vendor's performance and compliance with agreed-upon security measures.",
            "objective": "5.3 Explain the processes associated with third-party risk assessment and management"
        },
        {
            "type": "multiple_choice",
            "question": "Which of the following is NOT a typical consequence of non-compliance with security regulations?",
            "options": ["Monetary fines", "Reputational damage", "Legal sanctions", "Increased market share"],
            "answer": "Increased market share",
            "objective": "5.4 Summarize elements of effective security compliance"
        },
        {
            "type": "true_false",
            "question": "Penetration testing and vulnerability scanning serve the same purpose and can be used interchangeably.",
            "answer": False,
            "objective": "5.5 Explain types and purposes of audits and assessments"
        },
    ]
}

# (load_progress, save_progress, select_questions, ask_question, quiz, show_progress, select_domains, and main loop)

if __name__ == "__main__":
    while True:
        print("\nCompTIA Security+ SY0-701 Practice Quiz")
        print("1. Start a new quiz")
        print("2. Show progress")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            selected_domains = select_domains()
            num_questions = int(input("How many questions per domain? (1-5): "))
            selected_questions = select_questions(questions, num_questions, selected_domains)
            incorrect_answers = quiz(selected_questions)
            review_incorrect(incorrect_answers)
        elif choice == "2":
            show_progress()
        elif choice == "3":
            print("Thank you for using the CompTIA Security+ SY0-701 Practice Quiz. Good luck with your exam!")
            break
        else:
            print("Invalid choice. Please try again.")
            
            

