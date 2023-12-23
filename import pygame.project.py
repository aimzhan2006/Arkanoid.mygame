import pygame
import sys

WIDTH, HEIGHT = 1000, 700  # ширина и высота
fps = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (128, 0, 128)  # Фиолетовый цвет

# Инициализация Pygame
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))  # Создаем окно для отображения игры
pygame.display.set_caption("Arkanoid")  # Заголовок окна
clock = pygame.time.Clock()  # Объект для управления частотой обновления кадров (FPS) в игре

# Параметры платформы
platform_width = 120  # ширина платформы
platform_height = 15  # высота платформы
platform_speed = 11  # скорость движения платформы

# Класс шарика
class Ball:
    def __init__(self, x, y, radius, color, speed_x, speed_y): #инициализация свойств
        self.x = x #Инициализация координаты x шарика
        self.y = y #Инициализация координаты y шарика
        self.radius = radius #Инициализация радиуса шарика
        self.color = color # Инициализация цвета шарика
        self.speed_x = speed_x # Инициализация скорости шарика по оси x
        self.speed_y = speed_y # Инициализация скорости шарика по оси y

    def move(self): #добавляет значения скорости
        # обновляет позицию шарика в соответствии со значениями его скорости.
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self, surface):  # Отрисовка круга (шарика) на заданной поверхности
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius) #Это позволяет отобразить шарик на экране в текущей его позиции с заданными параметрами

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

ball_radius = 10
ball_speed_x = 5
ball_speed_y = 5
ball = Ball(WIDTH // 2, HEIGHT // 2, ball_radius, WHITE, ball_speed_x, ball_speed_y)  # Создаем экземпляр класса шарика

platform = pygame.Rect( #Этот код создаёт прямоугольник с помощью класса Rect
    WIDTH // 2 - platform_width // 2,  # X-координата левого края платформы
    HEIGHT - platform_height - 10,    # Y-координата верхнего края платформы
    platform_width,                   # Ширина платформы
    platform_height                   # Высота платформы
)


game_over = False  # Переменная для проверки окончания игры

while not game_over: #Цикл while выполняется, пока game_over не станет True.
    for event in pygame.event.get():  # Обработка событий
        if event.type == pygame.QUIT: # Проверяется тип события. Если происходит событие выхода из игры (например, нажатие на кнопку закрытия окна), то выполняются следующие действия:
            pygame.quit() #Это функция Pygame, которая завершает работу Pygame.
            sys.exit() #Это функция Pygame, которая завершает работу Pygame.

    keys = pygame.key.get_pressed()  # Получаем состояние клавиш
    if keys[pygame.K_LEFT] and platform.left > 0:  # Движение влево
        platform.x -= platform_speed
    if keys[pygame.K_RIGHT] and platform.right < WIDTH:  # Движение вправо
        platform.x += platform_speed

    ball.move()  # Движение шарика

    # Обработка отскока шарика от границ окна и платформы
    #
 #Этот фрагмент кода отвечает за обработку столкновений шарика с границами окна игры и платформой,
    # а также за условие завершения игры, если шарик выходит за нижнюю границу экрана.
    if ball.x - ball.radius <= 0 or ball.x + ball.radius >= WIDTH: #проверяет столкновения шарика со стенами по горизонтали
        ball.speed_x *= -1
    if ball.y - ball.radius <= 0:
        ball.speed_y *= -1
    elif ball.y + ball.radius >= HEIGHT:  # Если шарик выходит за нижнюю границу экрана - завершаем игру
        game_over = True

    ball_rect = ball.get_rect()  # Получаем прямоугольник шарика
    #Это позволяет обнаруживать столкновения с другими прямоугольниками, такими как платформа
    if ball_rect.colliderect(platform):  # Проверяем столкновение шарика и платформы
        ball.speed_y *= -1 #Если столкновение обнаружено, это меняет вертикальную скорость шарика на противоположную

    sc.fill(BLACK)  #экран черный

    pygame.draw.rect(sc, WHITE, platform)  # Отрисовка платформы

    ball.draw(sc)  # Отрисовка шарика

    pygame.display.flip()  # Обновление экрана
    clock.tick(fps)  # Управление частотой кадров

# Код выполняется после завершения игры (когда game_over == True)
# Добавляем сообщение об окончании игры
font = pygame.font.Font(None, 36) #Создаёт объект шрифта с размером 36
text = font.render("Game Over!", True, WHITE) #Эта строка генерирует изображение текста "Game Over!"
# с использованием ранее созданного объекта шрифта. Цвет текста указан как WHITE (предположительно, это определённый цвет).
text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2)) #Получает прямоугольник, описывающий размеры и позицию текста "Game Over!"
sc.blit(text, text_rect) #Рисует текст "Game Over!" на поверхности sc в позиции, указанной в text_rect.
pygame.display.flip() #последнее обновление

# Задержка перед закрытием окна
pygame.time.delay(2000)  # 2000 миллисекунд (2 секунды)
pygame.quit()
sys.exit()