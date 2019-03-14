
# object_on="plus"
object_on="wchen"


type_on="test"
# type_on="china"
# type_on="split_test"
# type_on="split_china"

if object_on=="plus":
    if type_on=="china":
        import PC_zonghe_selenium.login.plus_china
        from_def=PC_zonghe_selenium.login.plus_china

    if type_on == "test":
        import PC_zonghe_selenium.login.plus_test
        from_def = PC_zonghe_selenium.login.plus_test

if object_on == "wchen":
    if type_on=="china":
        import PC_zonghe_selenium.login.wchen_china
        from_def = PC_zonghe_selenium.login.wchen_china

    if type_on == "test":
        import PC_zonghe_selenium.login.wchen_test
        from_def = PC_zonghe_selenium.login.wchen_test

    if type_on == "split_china":
        import PC_zonghe_selenium.login.wchen_split_china
        from_def = PC_zonghe_selenium.login.wchen_split_china

    if type_on == "split_test":
        import PC_zonghe_selenium.login.wchen_split_test
        from_def = PC_zonghe_selenium.login.wchen_split_test


