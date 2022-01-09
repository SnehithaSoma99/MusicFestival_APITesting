import pytest
#import jsonpath_ng

class Test_ea_api:
    # Test 1 - Checking API Response code is 200
    # @pytest.mark.skip
    def test_api_responseCode_success(self, setup):
        self.response = setup
        print(f"API Response code {self.response.status_code}")
        print(self.response.json())
        assert self.response.status_code == 200, "API Response code is not 200"

    # @pytest.mark.skip
    def test_No_of_musicFestivals(self, setup):
        # Test 2 - Test verify  the Number if music festivals  returned by the API are 5):
        self.response = setup
        print(f"API Response code {self.response.status_code}")
        data = self.response.json()
        if len(data)==0:
            assert False, "Empty response received from the API"
        print("----API Response---")
        print(data)
        print("------------------")
        print(f"test_No_of_musicFestivals {len(data)}")
        assert len(data) == 5, "Expected Music festivals are 5 but API returned festivals are not 5"

    # @pytest.mark.skip
    def test_music_festival_names(self, setup):
        # Test 3 - Verify all music festival names:
        self.response = setup
        print(f"API Response code {self.response.status_code}")
        data = self.response.json()
        if len(data)==0:
            assert False, "Empty response received from the API"
        print("----API Response---")
        print(data)
        print("------------------")
        temp_list = []
        print(f"Total no of musical festivals {len(data)}")
        for val in range(0, len(data)):
            if 'name' in data[val]:
                temp_list.append(data[val]['name'])
        print(f"No of musical festivals which has name : {len(temp_list)}")
        assert len(data) ==len(temp_list), "All Musical Festivals do not have names"

    # @pytest.mark.skip
    def test_bands(self,setup):
        # Test 4 - Verify all Musical Festivals have bands:
        self.response = setup
        print(f"API Response code {self.response.status_code}")
        data = self.response.json()
        if len(data)==0:
            assert False, "Empty response received from the API"

        print("----API Response---")
        print(data)
        print("------------------")
        band_list = []
        print(f"Total no of musical festivals {len(data)}")
        for val in range(0, len(data)):
            if 'bands' in data[val]:
                band_list.append(data[val]['bands'])
        print(f"No of musical festivals which has name : {len(band_list)}")
        assert len(data) == len(band_list), "All  musical Festivals  do not have bands"

    # @pytest.mark.skip
    #Test 5 - Verifying the number of bands as expected in the response
    def test_No_of_bands_in_each_music_Festivals(self,setup):
        self.response = setup
        print(f"API Response code {self.response.status_code}")
        data = self.response.json()
        if len(data)==0:
            assert False, "Empty response received from the API"
        print("----API Response---")
        print(data)
        print("------------------")
        exepected_bands_in_each_music_festivals = {
            "LOL-palooza": 4,
            "Small Night In": 5,
            "Trainerella": 4,
            "Twisted Tour": 3,
            "": 2
        }
        actual_bands_in_each_music_festivals = {}
        for val in range(0, len(data)):
            if 'bands' in data[val]:
                if 'name' in data[val]:
                    actual_bands_in_each_music_festivals[data[val]['name']] = len(data[val]['bands'])
                else:
                    actual_bands_in_each_music_festivals[''] = len(data[val]['bands'])

        print(actual_bands_in_each_music_festivals)
        assert actual_bands_in_each_music_festivals.__eq__(exepected_bands_in_each_music_festivals), "Expected No of Music bands in the music festivals are mot matching"





