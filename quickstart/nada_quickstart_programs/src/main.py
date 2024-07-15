from nada_dsl import *

def nada_main():
    # Define parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    party4 = Party(name="Party4")
    party5 = Party(name="Party5")

    # Define secret integers
    a = SecretInteger(Input(name="A", party=party1))
    b = SecretInteger(Input(name="B", party=party2))
    c = SecretInteger(Input(name="C", party=party3))
    d = SecretInteger(Input(name="D", party=party4))

    # Perform operations
    sum_ab = a + b
    diff_cd = c - d
    prod_ac = a * c
    div_bd = b / d

    # Perform a combined operation
    combined_result = (sum_ab * diff_cd) + prod_ac - div_bd

    # Generate outputs
    output1 = Output(sum_ab, "sum_ab_output", party5)
    output2 = Output(diff_cd, "diff_cd_output", party5)
    output3 = Output(prod_ac, "prod_ac_output", party5)
    output4 = Output(div_bd, "div_bd_output", party5)
    output5 = Output(combined_result, "combined_result_output", party5)

    return [output1, output2, output3, output4, output5]
