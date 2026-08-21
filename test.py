from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent
#from backend import get_llm




# res = search_flights("Plan a 7 days Nepal trip from Bangladesh")
# print(res)

input_msg = input("Enter travel request: ")

response = run_travel_agent(
    user_input=input_msg,
    thread_id="test_user"
)

print("\nFINAL RESPONSE:\n")
print(response["answer"])
