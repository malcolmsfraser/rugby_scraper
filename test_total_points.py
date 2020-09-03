"""
Your module description
"""
from click.testing import CliRunner
from total_points import call_all_points

def test_call_all_points():
    runner = CliRunner()
    result = runner.invoke(call_all_points, ['--file', '.test.csv'])
    assert result.exit_code == 0
    assert 'Sunwolves: 101' in result.output
    assert 'Bulls: 115' in result.output
    assert 'Lions: 109' in result.output
    