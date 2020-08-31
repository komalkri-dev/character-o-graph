import turtle
import A_to_J
import K_to_S
import T_to_Z
import special_char

def display(name):
    window = turtle.Screen()
    window.screensize(1300, 800)
    window.bgcolor('black')

    offset = 0 - (len(name)*28)

    name = name.lower()

    for i in name:
        if i == 'a':
            A_to_J.draw_A(offset)
            offset = offset + 56
        if i == 'b':
            A_to_J.draw_B(offset)
            offset = offset + 56
        if i == 'c':
            A_to_J.draw_C(offset)
            offset = offset + 56
        if i == 'd':
            A_to_J.draw_D(offset)
            offset = offset + 56
        if i == 'e':
            A_to_J.draw_E(offset)
            offset = offset + 56
        if i == 'f':
            A_to_J.draw_F(offset)
            offset = offset + 56
        if i == 'g':
            A_to_J.draw_G(offset)
            offset = offset + 56
        if i == 'h':
            A_to_J.draw_H(offset)
            offset = offset + 56
        if i == 'i':
            A_to_J.draw_I(offset)
            offset = offset + 40
        if i == 'j':
            A_to_J.draw_J(offset)
            offset = offset + 56
        if i == 'k':
            K_to_S.draw_K(offset)
            offset = offset + 56
        if i == 'l':
            K_to_S.draw_L(offset)
            offset = offset + 56
        if i == 'm':
            K_to_S.draw_M(offset)
            offset = offset + 70

        if i == 'n':
            K_to_S.draw_N(offset)
            offset = offset + 56
        if i == 'o':
            K_to_S.draw_O(offset)
            offset = offset + 56
        if i == 'p':
            K_to_S.draw_P(offset)
            offset = offset + 56
        if i == 'q':
            K_to_S.draw_Q(offset)
            offset = offset + 56
        if i == 'r':
            K_to_S.draw_R(offset)
            offset = offset + 56
        if i == 's':
            K_to_S.draw_S(offset)
            offset = offset + 56
        if i == 't':
            T_to_Z.draw_T(offset)
            offset = offset + 56
        if i == 'u':
            T_to_Z.draw_U(offset)
            offset = offset + 56
        if i == 'v':
            T_to_Z.draw_V(offset)
            offset = offset + 56
        if i == 'w':
            T_to_Z.draw_W(offset)
            offset = offset + 84
        if i == 'x':
            T_to_Z.draw_X(offset)
            offset = offset + 56
        if i == 'y':
            T_to_Z.draw_Y(offset)
            offset = offset + 56
        if i == 'z':
            T_to_Z.draw_Z(offset)
            offset = offset + 56

        if i == ' ':
            special_char.draw_space(offset)
            offset = offset + 42
        if i == '.':
            special_char.draw_dot(offset)
            offset = offset + 14
        if i == '-':
            special_char.draw_dash(offset)
            offset = offset + 56
    
    window.exitonclick()

    return