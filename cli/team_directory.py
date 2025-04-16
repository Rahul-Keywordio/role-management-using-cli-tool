
"""First way with Cli framework Click"""

##################################################################################################

import click
from tabulate import tabulate


# teams = {}
# group_members = []
teams = [{
    "name": "developer-frontend",
    "description": "handles UI",
    "members": []

}]

group_members = [{
    "name": 'rahul',
    "email": "rahul@keywordio.com",
    "role": "intern",
    "team": "developer-frontend"
},
{
    "name": 'shubham',
    "email": "shubham@keywordio.com",
    "role": "intern",
    "team": "developer-backend"

},
{
    "name": 'karan',
    "email": "karan@keywordio.com",
    "role": "developer",
    "team": "senior-team"
}]

@click.group()
def cli():
    pass

@cli.command('add-team')
@click.option('--name',help='add by team name')
@click.option('--description',help='add description')
def add_team(name,description):
  
    team = {
        "name":name,
        "description":description,
        "members": [],
    }
    teams.append(team)
    click.echo(f'Team name {name} successfully added!')
  

@cli.command('list-teams')
def list_teams():
  
    if not teams:
        click.echo("No teams")
    else:
        for team in teams:
            temp = []
            temp.append([team["name"]])
            click.echo(temp)

@cli.command('add-member')
@click.option('--name')
@click.option('--email')
@click.option('--role')
@click.option('--team')
def add_members(name,email,role,team):
 
    member = {"name":name,
              "email":email,
              "role":role,
              "team":team,
              }
    group_members.append(member)
    for team in teams:
        if team["name"] == team:
            team["members"].append(member)
    click.echo(f'Member {name} is added to the team {team}')
     


@cli.command('list-members')
@click.option('--role',help='filter member by role')
@click.option('--team',help='filter member by team')
def list_members(role,team):
   
    filtered = []
    if team:
        for t in group_members:
            if t["team"] == team:
                filtered.append(t)
    elif role:
        for t in group_members:
            if t["role"] == role:
                filtered.append(t)
    if not filtered:
        click.echo("No matching members found")
    else:
        table_data = []
        for i in filtered:
            table_data.append([i["name"], i["email"], i["role"], i["team"]])
        click.echo(tabulate(table_data,headers=["Name", "Email", "Role", "Team"]))

@cli.command('assign-task')
def assign_task():
    click.echo("New task coming soon.......")

if __name__ == '__main__':
    cli()




######################################################################################################################################################

"""Second way without any cli framework"""


# teams = []
# members = []

# def add_team(name, description):
#     team = {'name': name, 'description':description,'members':[]}
#     teams.append(team)
#     print("Team added successfully") 

# def list_teams():
#     if not teams:
#         print("No teams available")
#     else:
#         for t in teams:
#             print(f"{t['name']}:{t['description']}")
    
# def add_member(name,role,team_name):
#     member = {'name':name,'role':role,'team_name':team_name}
#     members.append(member)

#     for t in teams:
#         if t['name']==team_name:
#             t['members'].append(member)
#     print(f"{name}added to the {team_name}")

# def filter_out(filter_team=None, filter_role= None):
#     filtered = members
#     if filter_team:
#         filtered = [person for person in filtered if person['team_name']==filter_team]
#     if filter_role:
#         filtered = [person for person in filtered if person['role']==filter_role]

#     if not filtered:
#         print("No matching record found!!!")

#     for person in filtered:
#         print(f"{person['name']} | Role:{person['role']} | Team:{person['team_name']}")

    
# def main_menu():
#     while True:
#         print("1. Add Team")
#         print("2. List Teams")
#         print("3. Add member")
#         print("4. list Members")
#         print("5. Exit")
        
#         choice = input("enter your choice from above given options:\n")
#         if choice == "1":
#             team = input("enter the team name:\n")
#             description = input("enter team description:\n")
#             add_team(team,description)
        
#         elif choice == "2":
#             list_teams()

#         elif choice == "3":
#             name = input("enter member name:\n")
#             role = input("enter role for the member:\n")
#             team_name = input("enter team name to add member into:\n")
#             add_member(name,role,team_name)
        
#         elif choice == "4":
#             filter_team = input("enter team you want to see or leave it blank:\n")
#             filter_role = input("enter role you want to see or leave it blank:\n")
#             filter_out(filter_team or None, filter_role or None)
#         elif choice == "5":
#             print("Good Bye!!!")
#             break
#         else:
#             print("Invalid Choice\n")

# if __name__=='__main__':
#     main_menu()
        



    
   

