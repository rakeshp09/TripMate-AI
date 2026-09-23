from backend import run_travel_agent

user_input =  input("Enter travel requests: ")
response = run_travel_agent(
    user_input,
    thread_id="test_user"
)

print("\n FINAL RESPONSE: \n")
print(response)



