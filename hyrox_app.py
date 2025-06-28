import streamlit as st

def hyrox_readiness(hours_workout, distance_run, run_pace, station_checklist):
    score = 0

    # endurance score
    if hours_workout >= 6:
        score += 30
    elif hours_workout >= 4:
        score += 20
    elif hours_workout >= 2:
        score += 10

    # running volume score
    if distance_run >= 25:
        score += 30
    elif distance_run >= 15:
        score += 20
    elif distance_run >= 5:
        score += 10

    # running pace score
    if run_pace <= 5:
        score += 20
    elif run_pace <= 6:
        score += 15
    elif run_pace <= 7:
        score += 10

    # HYROX station readiness
    completed_stations = sum(station_checklist)
    score += completed_stations * 2

    # readiness level
    if score >= 85:
        return "HYROX Elite"
    elif score >= 65:
        return "HYROX Competitor"
    elif score >= 45:
        return "HYROX Beginner"
    else:
        return "Not Ready Yet"

# Streamlit app layout
st.title("🏋️ HYROX Readiness Checker")

hours = st.number_input("How many hours do you train per week?", min_value=0.0)
km_run = st.number_input("How many km do you run per week?", min_value=0.0)
pace = st.number_input("What is your average 1km run pace (min/km)?", min_value=0.0)

st.write("Can you complete these HYROX stations?")
stations = [
    "SkiErg", "Sled Push", "Sled Pull", "Burpee Broad Jumps",
    "Rowing", "Farmers Carry", "Sandbag Lunges", "Wall Balls"
]

station_checklist = []
for station in stations:
    answer = st.radio(f"{station}:", options=["Yes", "No"], key=station)
    station_checklist.append(answer.lower() == "yes")

if st.button("Check Readiness"):
    result = hyrox_readiness(hours, km_run, pace, station_checklist)
    st.success(f"Your HYROX readiness level is: **{result}**")
