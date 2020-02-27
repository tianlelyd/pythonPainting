# 七段数码管实例
# Seven Digital Tube

import turtle as t
import time
tt = t.Screen()
# 定义函数规定每个数字对应的七段位置
def digital_number(number) :
    digital_tube = {
        0 : ['a', 'b', 'c', 'd', 'e', 'f'],
        1 : ['b', 'c'],
        2 : ['a', 'b', 'g', 'e', 'd'],
        3 : ['a', 'b', 'c', 'd', 'g'],
        4 : ['b', 'c', 'g', 'f'],
        5 : ['a', 'f', 'g', 'c', 'd'],
        6 : ['a', 'f', 'e', 'g', 'c', 'd'],
        7 : ['a', 'b', 'c'],
        8 : ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        9 : ['a', 'b', 'c', 'd', 'f', 'g']}
    return digital_tube.get(number)

# 根据turtule的右方向和长度画线
def right_lines(length, degree) :
    digitaler.pd()
    digitaler.right(degree)
    digitaler.fd(length)
    digitaler.pu()

# 划一根指定长度的线
def lines(length) :
    tabler.pd()
    tabler.fd(length)
    tabler.pu()

# 在指定位置画出指定半径的圆点
def d_dot(x, y, dot_radius, color = 'red') :
    dotor.pu()
    dotor.goto(x,y)
    dotor.dot(dot_radius, color)

# 画单独的一根数码管
def one_digital_tube(x, y, heading, m, n, color = 'red'):
    digitaler.pu()
    digitaler.goto(x, y)
    digitaler.pensize(1)
    digitaler.color(color)
    digitaler.seth(heading)
    digitaler.begin_fill()
    right_lines(m, 0)
    right_lines(n, 45)
    right_lines(n, 90)
    right_lines(m, 45)
    right_lines(n, 45)
    right_lines(n, 90)
    digitaler.end_fill()

# 数码管之间的相对位置
def digital_tube_position(s, m, n, k) :
    position = {
        'a' : (lambda x : x, lambda y : y, 0, m, n),
        'b' : (lambda x : x + m + k + 1.414*n, lambda y : y - 1.414*n - k, -90, m, n),
        'c' : (lambda x : x + m + k + 1.414*n, lambda y : y - 2.828*n -3*k - m, -90, m, n),
        'd' : (lambda x : x, lambda y : y - 2.828*n - 4*k - 2*m, 0, m, n),
        'e' : (lambda x : x - k, lambda y : y - 2.828*n -3*k - m, -90, m, n),
        'f' : (lambda x : x - k, lambda y : y - 1.414*n - k, -90, m, n),
        'g' : (lambda x : x, lambda y : y - 1.414*n - 2*k -m, 0, m, n)}
    return position.get(s)

# 给定位置参数（x,y）和数字参数，用于在指定位置开始画出数码管
def seven_digital_tube(x, y, number, m, n, k) :
    d_num = digital_number(number)
    for _i in d_num :
        d_t_pos = digital_tube_position(_i, m, n, k)
        one_d_tube = one_digital_tube(d_t_pos[0](x), d_t_pos[1](y), d_t_pos[2], d_t_pos[3], d_t_pos[4], (199/255, 199/255, 199/255))

# 计算表盘尺寸及各组件的相对位置，并返回相应数据
def calculate_table_size(m, n, k, p) :
    # 一个完整的数码管的尺寸
    d_length = m + 2*1.414*n + 2*k
    d_width = 2*m + 3*1.414*n + 4*k
    # 日期表盘的长宽
    date_table_length = d_length + 2*p
    date_table_width = d_width + 2*p
    # 时间表盘的长宽
    time_table_length = 6*d_length + 9*p
    time_table_width = d_width + 2*p
    # 完整的表盘数据长宽
    table_length = d_length*7 + 14*p
    table_width = d_width + 4*p
    # 完整表表盘的起始点(x, y)
    table_x = -table_length/2
    table_y = table_width/2
    # 日期表盘起始点(x, y)
    date_table_x = table_x + p
    date_table_y = table_y - p
    # 日期表盘内显示日期数据的起始点(x, y)
    date_table_in_x_y = []
    for i in range(1,5) :
        date_table_in_x_y.append((date_table_x + 6.2*p, date_table_y - p - i*d_width/4))
    # 时间表盘起始点(x, y)
    time_table_x = table_x + 2*p + date_table_length
    time_table_y = table_y - p
    # 时间表盘内显示数码管的起始位置(x, y)，有6个,第2个和第四个之后多增一个p距离，用于画时间分号
    time_table_in_x_y = [(time_table_x + p + 1.414*n + k, time_table_y - p)]
    for i in range(1,6) :
        time_table_in_x_y.append((time_table_in_x_y[i - 1][0] + d_length + p + (p if i%2 == 0 else 0), time_table_y - p))
    # 时间表盘中的冒号位置
    time_dot_x_y = []
    for i in range(1,4,2) :
        time_dot_x_y.append((time_table_in_x_y[i][0] -1.414*n -k + d_length + p, m/2))
        time_dot_x_y.append((time_table_in_x_y[i][0] -1.414*n -k + d_length + p, -m/2))
    return [
        (table_x, table_y, table_length, table_width), # 最外部表框的参数（起始位置，长和宽）
        (date_table_x, date_table_y, date_table_length, date_table_width), # 日期表框的参数（起始位置，长和宽）
        (time_table_x, time_table_y, time_table_length, time_table_width), # 时间表框的参数（起始位置，长和宽）
        time_table_in_x_y, time_dot_x_y, date_table_in_x_y] # 七段数码管的起始位置，时间分割冒号的起始位置，日期相应数据的起始位置

# 定义绘制表盘框函数
def draw_table(x, y, length, width, radius, pen_size, pen_color) :
    tabler.pu()
    tabler.pensize(pen_size)
    tabler.pencolor(pen_color)
    tabler.goto(x, y)
    tabler.pd()
    for i in range(2) :
        lines(length)
        tabler.pd()
        tabler.circle(-radius, 90)
        lines(width)
        tabler.pd()
        tabler.circle(-radius, 90)
        tabler.pu()

# 月份和星期的获取
def get_months(s) :
    months = {
        'Jan' : '一',
        'Feb' : '二',
        'Mar' : '三',
        'Apr' : '四',
        'May' : '五',
        'Jun' : '六',
        'Jul' : '七',
        'Aug' : '八',
        'Sep' : '九',
        'Oct' : '十',
        'Nov' : '十一',
        'Dec' : '十二'}
    return months.get(s)
def get_weeks(s) :
    weeks = {
        'Mon' : '一',
        'Tue' : '二',
        'Wed' : '三',
        'Thur' : '四',
        'Fri' : '五',
        'Sat' : '六',
        'Sun' : '日'}
    return weeks.get(s)
# 获取时间，并进行格式处理
def get_date_time():
    time_number = []
    date_list = []
    time_list = time.ctime().split(' ')
    for i in time_list[3] :
        if i != ':' :
            time_number.append(int(i))
    date_list.append((time_list[4], '年'))
    date_list.append((get_months(time_list[1]), '月'))
    date_list.append((time_list[2], '日'))
    date_list.append(('星期', get_weeks(time_list[0])))
    return time_number, date_list


# 绘制钟表表盘
def draw_clock(m, n, k, p):
    global tabler, digitaler, writer, dotor, c_t_size
    c_t_size = calculate_table_size(m, n, k, p) # 获取表框的相应参数
    
    # 创建一个表框Turtle对象
    tabler = t.Turtle()
    tabler.hideturtle()
    tabler.pu()
    # 绘制外表盘，四周倒圆角,圆角的半径定为10，线框的线宽8
    draw_table(c_t_size[0][0] + 10, c_t_size[0][1], c_t_size[0][2] - 20, c_t_size[0][3] - 20, 10, 8, (232/255, 232/255, 232/255))
    # 绘制日期表盘，四周倒圆角,圆角的半径定为10，线框的线宽5
    draw_table(c_t_size[1][0] + 10, c_t_size[1][1], c_t_size[1][2] - 20, c_t_size[1][3] -20 , 10, 2, (232/255, 232/255, 232/255))
    # 绘制时间表盘，四周倒圆角,圆角的半径定为10，线框的线宽5
    draw_table(c_t_size[2][0] + 10, c_t_size[2][1], c_t_size[2][2] - 20, c_t_size[2][3] -20 , 10, 2, (232/255, 232/255, 232/255))
    # 创建一个时间冒号Turtle对象
    dotor = t.Turtle()
    # 创建一个绘制数码管对象
    digitaler = t.Turtle()
    # 创建一个书写Turtle对象
    writer = t.Turtle()

# 初始化turtle
t.hideturtle()


def tick() :
    g_d_time = get_date_time() # 获取时间相应参数
    # 写入日期相关的数据 
    tt.tracer(False)
    writer.clear()
    writer.hideturtle()
    writer.pu()
    for i in range(4) :
        writer.pencolor(156/255, 156/255, 156/255)
        writer.goto(c_t_size[5][i][0], c_t_size[5][i][1])
        writer.write('{} {}'.format(g_d_time[1][i][0],g_d_time[1][i][1]), align="right", font=('Arial', 11, 'normal'))
    tt.tracer(10)
    tt.update()
    # 绘制6个时间数码管
    digitaler.clear()
    digitaler.hideturtle()
    digitaler.pu()
    t.speed(20)
    for i in range(6) :
        seven_digital_tube(c_t_size[3][i][0],c_t_size[3][i][1], g_d_time[0][i], m, n, k)
    tt.tracer(10)
    tt.update()
    # 绘制时间冒号
    dotor.clear()
    dotor.hideturtle()
    dotor.pu()
    # 如果最后一位数字是偶数，显示两个冒号，否则只显示前面一个冒号
    if g_d_time[0][5] % 2 == 0 :
        for i in range(4) :
            d_dot(c_t_size[4][i][0], c_t_size[4][i][1], 5, (212/255, 212/255, 212/255))
    else :
        for i in range(2) :
            d_dot(c_t_size[4][i][0], c_t_size[4][i][1], 5, (212/255, 212/255, 212/255))
    tt.tracer(10)
    tt.update()
    tt.ontimer(tick, 100)

# 设定各参数
m = 30  # 单个数码管的长度
n = 6  # 单个数码管的宽度
k = 3   # 单个数码管之间的间隔
p = 10 # 完整数码管之间的间隔,表盘之间的间隔

def main() :
    tt.tracer(False)
    draw_clock(m, n, k, p)
    tt.update()
    tick()
    tt.mainloop()

if __name__ == '__main__':
    main()

# 好尴尬，画的好慢，和电脑上显示的不一样，电脑感觉是瞬间刷新，直接显现的