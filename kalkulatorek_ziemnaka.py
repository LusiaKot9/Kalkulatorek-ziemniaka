import pygame as p
import pygame.rect

screen_width = 720
screen_height = 940
screen =p.display.set_mode((screen_width, screen_height))
pygame.font.init()
font_przycisk_ziemniak = pygame.font.Font(size = 40)
dzialanie = ''
easter_egg_activated = False
class Przycisk:
    def __init__(self, x, y, tekst):
        self.x = x
        self.y = y
        self.tekst = tekst
        self.rect = pygame.rect.Rect(self.x, self.y, 100, 100)

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
def tekst_dla_leniwych(zawartosc, kolor, screen,x,y):
    zawartosc_render = font_przycisk_ziemniak.render(zawartosc, True, kolor)
    szerokosc_zawartosc = zawartosc_render.get_width()
    screen.blit(zawartosc_render, (x - szerokosc_zawartosc, y))
def easter_egg (dzialanie, screen,):
    global easter_egg_activated
    if '14253680' in dzialanie:
        tekst_dla_leniwych("Użyj KLAWIATURY by uzyskać pełną moc!!!", "#751016", screen, 670, 260)
        easter_egg_activated = True
    else:
        easter_egg_activated = False
def ooograniczeeenie_działaaań (znaaaczeeek):
    global dzialanie
    if dzialanie[-1] in ["+","-","*","/"]:
        dzialanie = dzialanie[0: -1] + znaaaczeeek









#hojem to przerwa pomiędzy linijkami
hejom = 140

przycisk_cofnik = Przycisk(40, 370, "<<")
przycisk_one = Przycisk(220,370,"1")
przycisk_two = Przycisk(400,370,"2")
przycisk_three = Przycisk(580,370,"3")
przycisk_równa_sie = Przycisk(40,370+hejom,"=")
przycisk_four = Przycisk(220,370+hejom,"4")
przycisk_five = Przycisk(400,370+hejom,"5")
przycisk_six = Przycisk(580,370+hejom,"6")
przycisk_razy = Przycisk(40,370+hejom+hejom,"*")
przycisk_seven = Przycisk(220,370+hejom+hejom,"7")
przycisk_eight = Przycisk(400,370+hejom+hejom,"8")
przycisk_nine = Przycisk(580,370+hejom+hejom,"9")
przycisk_plus = Przycisk(40,370+hejom+hejom+hejom,"+")
przycisk_minus = Przycisk(220,370+hejom+hejom+hejom,"-")
przycisk_zero = Przycisk(400,370+hejom+hejom+hejom,"0")
przycisk_slash = Przycisk(580,370+hejom+hejom+hejom,"/")
ekran = pygame.rect.Rect(40, 40, 640,250 )
przyciski_do_druku = [przycisk_zero, przycisk_one, przycisk_two, przycisk_three, przycisk_four,
                      przycisk_five, przycisk_six, przycisk_seven, przycisk_eight, przycisk_nine,
                      przycisk_razy, przycisk_slash, przycisk_plus, przycisk_minus]


ziemniak_kal = True

while ziemniak_kal:
    screen.fill("black")
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
                    dzialanie += przycisk.tekst
                    # ooograniczeeenie_działaaań("błąd systemu")
            if przycisk_cofnik.click(pozycja):
                dzialanie = dzialanie[0 : -1]




    pygame.draw.rect(screen, "#222222", ekran)
    if easter_egg_activated == False:
        tekst_dla_leniwych(dzialanie,"white", screen, 670, 260)
    easter_egg(dzialanie,screen)
    przycisk_równa_sie.draw(screen)
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
    pygame.display.update()











