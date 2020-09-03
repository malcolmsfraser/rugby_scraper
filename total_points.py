"""
Your module description
"""
import click
import pandas as pd

def all_points(file):
    all_matches = pd.read_csv(file)
    total_points_scored = dict.fromkeys(set(all_matches['Home Team']),0)
    for i in range(len(all_matches)):
        total_points_scored[all_matches.iloc[i]['Home Team']] += all_matches.iloc[i]['Home Team Score']
        total_points_scored[all_matches.iloc[i]['Away Team']] += all_matches.iloc[i]['Away Team Score']
        pass
    result = [f'{team}: {score}' for team,score in total_points_scored.items()]
    result = '\n'.join(result)
    return result

# if __name__ == '__main__':
#     print(all_points('super_rugby/rugby.csv'))

@click.command()
@click.option('--file')
def call_all_points(file):
    results = all_points(file)
    print(results)
    pass

if __name__ == '__main__':
    call_all_points()