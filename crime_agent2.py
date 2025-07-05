crime_data = {
    "suspects": [
        {"name": "Vincent 'Vince' Carter", "dob": "12/08/1989", "father": "Richard Carter", "address": "Unknown", "involvement": "Primary suspect; prior armed robbery convictions, identified via partial facial match."},
        {"name": "Marcus 'Rook' Delgado", "dob": "05/22/1993", "father": "Hector Delgado", "address": "1123 Oak Lane, Southside", "involvement": "Suspected getaway driver; linked via abandoned SUV tire marks."},
        {"name": "Sophia Reynolds", "dob": "09/14/1995", "father": "James Reynolds", "address": "330 Diamond Plaza Apt 4B", "involvement": "Ex-employee; suspected inside help (terminated 2 months prior)."},
        {"name": "Unidentified Male", "dob": "N/A", "father": "N/A", "address": "Unknown", "involvement": "Eyewitnesses describe him as the third robber with an Eastern European accent."}
    ],
    "witness_testimonies": [
        {"name": "Daniel K. Mitchell", "age": 42, "testimony": "The tallest suspect (6'2 approx had a deep Eastern European accent. He pointed the shotgun at me while the others emptied the vault."},
        {"name": "Priya S. Patel", "age": 28, "testimony": "One robber had a tattoo on his left wrist—a skull with wings. They yelled 'Nobody moves!' before smashing the glass."},
        {"name": "Officer Jake T. Hurley", "age": 35, "testimony": "The SUV sped off toward 7th Street. We found it within 15 minutes, but the suspects had already fled on foot."}
    ],
    "ballistic_evidence": [
        "Two 9mm pistols (serial numbers filed off, suspected black market purchase).",
        "Sawed-off shotgun (12-gauge, recovered from the SUV with partial fingerprints).",
        "Crowbar (used to smash display cases, left at the scene with DNA traces)."
    ],
    "stolen_items": {
        "Cash (from SUV)": {"value": "$320,000", "status": "Recovered"},
        "Diamond Necklace": {"value": "$850,000", "status": "Missing"},
        "Luxury Watches (x12)": {"value": "$1.1 million", "status": "Missing"},
        "Gold Rings (x25)": {"value": "$230,000", "status": "Missing"}
    },
    "international_coordination": "International alert for possible cross-border sale of stolen goods."
}

"""GIVEN DATA IN THE FORM OF A DICTIONARY WRITTEN IN CODE FORMAT"""

def answer_queries():
    print("\n1. Distinguishing physical features of suspects:")
    for testimony in crime_data["witness_testimonies"]:
        print(f"- {testimony['testimony']}")

    print("\n2. Connection between Sophia Reynolds and the crime scene:")
    for suspect in crime_data["suspects"]:
        if "Sophia Reynolds" in suspect["name"]:
            print(f"- {suspect['involvement']}")

    print("\n3. Ballistic evidence recovered from the abandoned vehicle:")
    for evidence in crime_data["ballistic_evidence"]:
        print(f"- {evidence}")

    print("\n4. Value of stolen property that remains unrecovered:")
    total_missing = 0  # Initialize total_missing to 0
    for item in crime_data["stolen_items"].values():
        if item["status"] == "Missing":
            value_str = item["value"].replace("$", "").replace(",", "")
            if "million" in value_str:
                # Handle values in millions
                value = float(value_str.replace(" million", "")) * 1000000
            else:
                value = int(value_str)  # Handle normal integer values
            total_missing += value
    print(f"- Total unrecovered value: ${total_missing:,}")

    print("\n5. International coordination details:")
    print(f"- {crime_data['international_coordination']}")

if __name__ == "__main__":
    answer_queries()