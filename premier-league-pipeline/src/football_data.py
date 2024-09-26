import pandas as pd

from service.football_data_service import FootballDataService

RESULT_MAPPING = {'HOME_TEAM': 0, 'DRAW': 1, 'AWAY_TEAM': 2}


def get_team_stats_df(football_data_service: FootballDataService,
                      get_dummies: bool = False,
                      seasons: list = ['2022', '2023']) -> pd.DataFrame:

    match_data = []

    for season in seasons:
        matches = football_data_service.get_matches(season=season)
        for match in matches:
            match_data.append({
                'date': match['utcDate'],
                'home_team': match['homeTeam']['shortName'],
                'away_team': match['awayTeam']['shortName'],
                'home_score': match['score']['fullTime']['home'],
                'away_score': match['score']['fullTime']['away'],
                'result': match['score']['winner'],
                'matchday': match['matchday']
            })

    df = pd.DataFrame(match_data)

    df['home_points'] = df.apply(calculate_home_points, axis=1)
    df['away_points'] = df.apply(calculate_away_points, axis=1)
    df['result'] = df['result'].map(RESULT_MAPPING)

    home_df = df[['date', 'home_team', 'home_score', 'away_score', 'home_points']].copy()
    home_df.columns = ['date', 'team', 'goals_for', 'goals_against', 'points']

    away_df = df[['date', 'away_team', 'away_score', 'home_score', 'away_points']].copy()
    away_df.columns = ['date', 'team', 'goals_for', 'goals_against', 'points']

    combined_df = pd.concat([home_df, away_df], ignore_index=True)

    combined_df = combined_df.sort_values(by=['team', 'date']).reset_index(drop=True)

    combined_df['form_last_5'] = combined_df.groupby('team')['points'].shift(
        1).rolling(window=5).sum().reset_index(0, drop=True)

    combined_df['avg_goals_for_last_5'] = combined_df.groupby(
        'team')['goals_for'].shift(1).rolling(window=5).mean().reset_index(0, drop=True)

    combined_df['avg_goals_against_last_5'] = combined_df.groupby(
        'team')['goals_against'].shift(1).rolling(window=5).mean().reset_index(0, drop=True)

    home_stats = combined_df[['date', 'team', 'form_last_5', 'avg_goals_for_last_5', 'avg_goals_against_last_5']].copy()
    away_stats = home_stats.copy()

    df = pd.merge(df, home_stats, how='left', left_on=['home_team', 'date'], right_on=['team', 'date'])
    df = df.rename(columns={
        'form_last_5': 'home_team_form_last_5',
        'avg_goals_for_last_5': 'home_team_avg_goals_for_last_5',
        'avg_goals_against_last_5': 'home_team_avg_goals_against_last_5'
    })

    df = pd.merge(df, away_stats, how='left', left_on=['away_team', 'date'], right_on=['team', 'date'])
    df = df.rename(columns={
        'form_last_5': 'away_team_form_last_5',
        'avg_goals_for_last_5': 'away_team_avg_goals_for_last_5',
        'avg_goals_against_last_5': 'away_team_avg_goals_against_last_5'
    })

    df = df.drop(columns=['team_x', 'team_y', 'home_points', 'away_points', 'home_score', 'away_score'], axis=1)

    if get_dummies:
        df = pd.get_dummies(df, columns=['home_team', 'away_team'], dtype=int)
    else:
        df = df.drop(columns=['home_team', 'away_team'], axis=1)

    df = df.dropna()

    return df


def calculate_home_points(row) -> int:
    if row['home_score'] > row['away_score']:
        return 3
    elif row['home_score'] == row['away_score']:
        return 1
    else:
        return 0


def calculate_away_points(row) -> int:
    if row['home_score'] < row['away_score']:
        return 3
    elif row['home_score'] == row['away_score']:
        return 1
    else:
        return 0


if __name__ == '__main__':
    football_data_service = FootballDataService()
    df = get_team_stats_df(football_data_service, get_dummies=True)
    print(df.shape)
