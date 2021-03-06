import json
from pathlib import Path

from click.testing import CliRunner

from routor import cli

from . import test_engine

EXPECTED_PATH = [
    [51.4996599, -2.6823824],
    [51.4995741, -2.6814815],
    [51.4994456, -2.6800409],
    [51.4993081, -2.6783377],
    [51.4991721, -2.6763069],
    [51.4991449, -2.675861],
    [51.4991271, -2.6754226],
    [51.4991331, -2.6751891],
    [51.4991554, -2.6749678],
    [51.4991941, -2.6747517],
    [51.4992383, -2.674607],
    [51.4992842, -2.6744903],
    [51.4993387, -2.6743712],
    [51.4994118, -2.674251],
    [51.4994798, -2.6741659],
    [51.49957, -2.6740695],
    [51.499665, -2.6739949],
    [51.4997755, -2.6739402],
    [51.4998636, -2.6739152],
    [51.4999821, -2.6739001],
    [51.5000958, -2.673914],
    [51.5001762, -2.6739405],
    [51.5002679, -2.6739825],
    [51.5003573, -2.6740456],
    [51.500427, -2.6741088],
    [51.5005061, -2.6741985],
    [51.5005879, -2.6743164],
    [51.5006426, -2.6744183],
    [51.5006969, -2.6745408],
    [51.5007484, -2.6746896],
    [51.5007817, -2.6748145],
    [51.500805, -2.6749644],
    [51.5008198, -2.6751174],
    [51.5008211, -2.675273],
    [51.5008187, -2.6754124],
    [51.5007989, -2.6755743],
    [51.5007602, -2.6757798],
    [51.5007085, -2.6759668],
    [51.5006484, -2.6761387],
    [51.5001678, -2.6771543],
    [51.4997238, -2.6781119],
    [51.4992678, -2.6791965],
    [51.4989541, -2.6798183],
    [51.4980328, -2.6816171],
    [51.4973375, -2.6828411],
]


def test_main(graph_path: Path):
    runner = CliRunner()
    origin = f"{test_engine.ORIGIN_LOCATION.latitude},{test_engine.ORIGIN_LOCATION.longitude}"
    destination = f"{test_engine.DESTINATION_LOCATION.latitude},{test_engine.DESTINATION_LOCATION.longitude}"

    result = runner.invoke(
        cli.route, [str(graph_path), origin, destination, "routor.weights.travel_time"]
    )
    assert result.exit_code == 0

    data = json.loads(result.output)
    expected_data = {
        "costs": 46.20,
        "length": 1449.67,
        "travel_time": 46.20,
        "path": [
            {"latitude": point[0], "longitude": point[1]} for point in EXPECTED_PATH
        ],
    }
    assert json.dumps(data, sort_keys=True) == json.dumps(expected_data, sort_keys=True)
