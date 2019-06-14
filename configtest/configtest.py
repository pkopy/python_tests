import configparser

def createConfig(path):
    '''
    Create a config file
    '''
    test = 'oooooo'
    config = configparser.RawConfigParser()
    config.add_section("Settings")
    config.set("Settings", "font", "Courier")
    config.set("Settings", "font_size", "10")
    config.set("Settings", "font_style", "Normal")
    config.set("Settings", "font_info", '%(font)s at %(font_size)s')

    config.add_section('Section1')
    config.set('Section1', 'an_int', '15')
    config.set('Section1', 'a_bool', 'true')
    config.set('Section1', 'a_float', '3.1415')
    config.set('Section1', 'baz', 'fun')
    config.set('Section1', 'bar', 'Python')
    config.set('Section1', 'foo', '%(bar)s is %(baz)s!')

    with open(path, "w") as config_file:
        config.write(config_file)

if __name__ == "__main__":
    path = 'settings.ini'
    
    createConfig(path)
    cfg = configparser.ConfigParser()
    cfg.read('setting.ini')
    print(cfg.get('Section1', 'foo', raw=True))