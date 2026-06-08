import pygame as p
import pygame.rect
import sympy

screen_width = 720
screen_height = 940
screen =p.display.set_mode((screen_width, screen_height))
pygame.font.init()
font_przycisk_ziemniak = pygame.font.Font(size = 40)
dzialanie = ''
historia = []
easter_egg_activated = False
historia_menu = False
class Przycisk:
    def __init__(self, x, y, tekst, key):
        self.x = x
        self.y = y
        self.tekst = tekst
        self.rect = pygame.rect.Rect(self.x, self.y, 100, 100)
        self.key = key

    def draw(self,screen):
        pygame.draw.rect(screen,"#39FF14",self.rect)
        napis = font_przycisk_ziemniak.render(self.tekst, True, 'black')
        #szerokość napisu jest mierzona w ZIEMNIAKCH 🍠🍠
        tekst_rect = napis.get_rect(center = self.rect.center)
        screen.blit(napis,tekst_rect)



        #klik_pos to pozycja myszki bo mój kot jest ślepy więc mu pomagam
    def click(self,klik_pos):
        if self.rect.collidepoint(klik_pos):
            return True
        else:
            return False
def tekst_dla_leniwych(zawartosc, kolor, screen,x,y,left_or_right = 'right'):
    zawartosc_render = font_przycisk_ziemniak.render(zawartosc, True, kolor)
    szerokosc_zawartosc = zawartosc_render.get_width()
    if left_or_right == 'right':
        screen.blit(zawartosc_render, (x - szerokosc_zawartosc, y))
    elif left_or_right == 'left':
        screen.blit(zawartosc_render, (x,y))
    else:
        error_render = font_przycisk_ziemniak.render('error 404 not found', True, kolor)
        screen.blit(error_render,(x,y))

def przycisk_historia(screen):
    rect = pygame.rect.Rect(570,0,150,40)
    pygame.draw.rect(screen,'red',rect)
    tekst_dla_leniwych('historia','white',screen,710,8)
    return rect
def przycisk_exit_historia(screen):
    rect = pygame.rect.Rect(570,0,150,40)
    pygame.draw.rect(screen, 'red', rect)
    tekst_dla_leniwych('exit', 'white', screen, 710, 16)
    return rect

def easter_egg (dzialanie, screen,):
    global easter_egg_activated
    if '14253680' in dzialanie:
        tekst_dla_leniwych("Użyj KLAWIATURY by uzyskać pełną moc!!!", "#751016", screen, 670, 260)
        easter_egg_activated = True
    elif "8*8*8*8*8*8" in dzialanie:
        tekst_dla_leniwych('hello','#751016', screen, 670, 260)
        easter_egg_activated = True
    elif "1+1+1+1+1+1" in dzialanie:
        tekst_dla_leniwych('hi', '#751016', screen, 670, 260)
        easter_egg_activated = True
    else:
        easter_egg_activated = False
def ooograniczeeenie_działaaań (zanaczek):
    global dzialanie
    if dzialanie:

        if dzialanie[-1] == '/' and zanaczek == '/':
            if dzialanie [-2] == '/' and zanaczek == '/':
                dzialanie = dzialanie[0: -1]

        elif dzialanie[-1] in ["+","-",'*','^','/','.'] and zanaczek in ["+","-",'*','^','/','.']:
            if dzialanie [-1] == '/' and dzialanie [-2] == '/':
                dzialanie = dzialanie [0: -2]
            else:
                dzialanie = dzialanie [0: -1]

def new_tab_historia(screen):
    for i in range(len(historia)):
        historia_sting = f"{historia[i]['dzialanie']} = {historia[i]['wynik']}"
        tekst_dla_leniwych(historia_sting, "white", screen, 0, i*30,'left')















#hojem to przerwa pomiędzy linijkami
hejom = 140

przycisk_cofnik = Przycisk(40, 370, "<<",pygame.K_BACKSPACE)
przycisk_one = Przycisk(220,370,"1", pygame.K_1)
przycisk_two = Przycisk(400,370,"2", pygame.K_2)
przycisk_three = Przycisk(580,370,"3", pygame.K_3)
przycisk_rowna_sie = Przycisk(40, 370 + hejom, "=", pygame.K_RETURN)
przycisk_four = Przycisk(220,370+hejom,"4", pygame.K_4)
przycisk_five = Przycisk(400,370+hejom,"5", pygame.K_5)
przycisk_six = Przycisk(580,370+hejom,"6", pygame.K_6)
przycisk_razy = Przycisk(40,370+hejom+hejom,"*", pygame.K_ASTERISK)
przycisk_seven = Przycisk(220,370+hejom+hejom,"7", pygame.K_7)
przycisk_eight = Przycisk(400,370+hejom+hejom,"8" , pygame.K_8)
przycisk_nine = Przycisk(580,370+hejom+hejom,"9" , pygame.K_9)
przycisk_plus = Przycisk(40,370+hejom+hejom+hejom,"+" , pygame.K_PLUS)
przycisk_minus = Przycisk(220,370+hejom+hejom+hejom,"-" , pygame.K_MINUS)
przycisk_zero = Przycisk(400,370+hejom+hejom+hejom,"0" , pygame.K_0)
przycisk_slash = Przycisk(580,370+hejom+hejom+hejom,"/" , pygame.K_SLASH)
ekran = pygame.rect.Rect(40, 40, 640,250 )
przyciski_do_druku = [przycisk_zero, przycisk_one, przycisk_two, przycisk_three, przycisk_four,
                      przycisk_five, przycisk_six, przycisk_seven, przycisk_eight, przycisk_nine,
                      przycisk_razy, przycisk_slash, przycisk_plus, przycisk_minus]


ziemniak_kal = True

while ziemniak_kal:
    screen.fill("black")
    przycisk_h = przycisk_historia(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ziemniak_kal = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pozycja = pygame.mouse.get_pos()
            # if przycisk_zero.click(pozycja):
            #     dzialanie += przycisk_zero.tekst
            # to była wersja 1

            for przycisk in przyciski_do_druku:
                if przycisk.click(pozycja):
                    ooograniczeeenie_działaaań(przycisk.tekst)
                    dzialanie += przycisk.tekst
            if przycisk_cofnik.click(pozycja):
                dzialanie = dzialanie[0 : -1]
            if przycisk_rowna_sie.click(pozycja):
                emelement = {'dzialanie': dzialanie}
                dzialanie = str(sympy.sympify(dzialanie).evalf()).rstrip('0').rstrip('.')
                if dzialanie == '':
                    dzialanie = '0'
                emelement['wynik'] = dzialanie
                historia.append(emelement)
                print(historia)
            if przycisk_h.collidepoint(pozycja):
                historia_menu = True
                print('malinka')





        if event.type == pygame.KEYDOWN:
            for przycisk in przyciski_do_druku:
                if event.key == przycisk.key and not pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    ooograniczeeenie_działaaań(przycisk.tekst)
                    dzialanie += przycisk.tekst
            if event.key == przycisk_cofnik.key:
                dzialanie = dzialanie[0 : -1]
            if event.key == pygame.K_8 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                ooograniczeeenie_działaaań('*')
                dzialanie += "*"
            elif event.key == pygame.K_EQUALS and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                ooograniczeeenie_działaaań('+')
                dzialanie += "+"
            elif event.key == pygame.K_9 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                ooograniczeeenie_działaaań('(')
                dzialanie += "("
            elif event.key == pygame.K_0 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                ooograniczeeenie_działaaań(')')
                dzialanie += ")"
            elif event.key == pygame.K_EQUALS:
                emelement = {'dzialanie': dzialanie}
                dzialanie = str(sympy.sympify(dzialanie).evalf()).rstrip('0').rstrip('.')
                emelement['wynik'] = dzialanie
                historia.append(emelement)
                print(historia)
            elif event.key == pygame.K_PERIOD or event.key == pygame.K_COMMA:
                ooograniczeeenie_działaaań('.')
                dzialanie += '.'
            elif event.key == pygame.K_6 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                ooograniczeeenie_działaaań('^')
                dzialanie += '^'








    pygame.draw.rect(screen, "#222222", ekran)
    if easter_egg_activated == False:
        tekst_dla_leniwych(dzialanie,"white", screen, 670, 260)

    easter_egg(dzialanie,screen)
    przycisk_rowna_sie.draw(screen)
    przycisk_one.draw(screen)
    przycisk_two.draw(screen)
    przycisk_three.draw(screen)
    przycisk_cofnik.draw(screen)
    przycisk_four.draw(screen)
    przycisk_five.draw(screen)
    przycisk_six.draw(screen)
    przycisk_razy.draw(screen)
    przycisk_seven.draw(screen)
    przycisk_eight.draw(screen)
    przycisk_nine.draw(screen)
    przycisk_slash.draw(screen)
    przycisk_plus.draw(screen)
    przycisk_minus.draw(screen)
    przycisk_zero.draw(screen)

    if historia_menu == True:
        screen.fill('black')
        new_tab_historia(screen)
        przycisk_h_exit = przycisk_exit_historia(screen)
        if przycisk_h_exit.collidepoint(pozycja):
            historia_menu = False
            print('jabłuszko')


    pygame.display.update()











