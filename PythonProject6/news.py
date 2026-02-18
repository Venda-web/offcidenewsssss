from flask import Flask, render_template_string

app = Flask(__name__)

# Новости только про футбол и хоккей
news_data = [
{
        'title': 'Килиан Мбаппе в интервью TNT Sports"',
        'date': '18 февраля 2025',
        'category': 'Футбол',
        'content': ' «Я считаю, что Джанлуке Престианни не следует приезжать на «Бернабеу», лучший стадион в мире»..'
    },
    {
        'title': 'Мурильо может перейти в Челси"',
        'date': '18 февраля 2025',
        'category': 'Футбол',
        'content': 'Сумма трансфера может составть около 70 млн фунтов.'
    },
    {
        'title': 'Месси сделал хет-трик в матче с "Реалом"',
        'date': '18 февраля 2025',
        'category': 'Футбол',
        'content': 'Лионель Месси забил три гола и принес победу "Барселоне" со счетом 3:1.'
    },
    {
        'title': 'Овечкин забил 800-й гол в НХЛ',
        'date': '18 февраля 2025',
        'category': 'Хоккей',
        'content': 'Российский форвард вышел на второе место в истории лиги по количеству заброшенных шайб.'
    },
    {
        'title': '"Спартак" обыграл ЦСКА в дерби',
        'date': '17 февраля 2025',
        'category': 'Футбол',
        'content': 'Красно-белые победили со счетом 2:1 в матче 18-го тура РПЛ.'
    },
    {
        'title': 'Малкин сделал три передачи в матче с "Рейнджерс"',
        'date': '17 февраля 2025',
        'category': 'Хоккей',
        'content': 'Евгений Малкин набрал 3 очка и был признан первой звездой матча.'
    },
    {
        'title': 'Мбаппе перешел в "Реал Мадрид"',
        'date': '16 февраля 2025',
        'category': 'Футбол',
        'content': 'Французский нападающий подписал контракт с мадридским клубом до 2029 года.'
    },
    {
        'title': 'Россия обыграла Канаду в финале Кубка Первого канала',
        'date': '16 февраля 2025',
        'category': 'Хоккей',
        'content': 'Сборная России по хоккею обыграла канадцев со счетом 4:2.'
    }
]

# Упрощенный HTML шаблон
TEMPLATE = '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Offcide News</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }

        body {
            background: #f0f2f5;
            padding: 20px;
        }

        .container {
            max-width: 1000px;
            margin: 0 auto;
        }

        /* Шапка */
        .header {
            background: #1a1a2e;
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            text-align: center;
        }

        .header h1 {
            font-size: 36px;
        }

        .header span {
            color: #e94560;
        }

        /* Кнопки фильтра */
        .filter {
            text-align: center;
            margin-bottom: 20px;
        }

        .filter-btn {
            background: white;
            border: none;
            padding: 10px 25px;
            margin: 0 5px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            border: 2px solid #1a1a2e;
        }

        .filter-btn.active {
            background: #1a1a2e;
            color: white;
        }

        /* Список новостей */
        .news-list {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        /* Карточка новости */
        .news-item {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            border-left: 5px solid #1a1a2e;
        }

        .news-item.football {
            border-left-color: #00b894;
        }

        .news-item.hockey {
            border-left-color: #e17055;
        }

        .news-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
            color: #666;
            font-size: 14px;
        }

        .news-category {
            font-weight: bold;
        }

        .news-category.football {
            color: #00b894;
        }

        .news-category.hockey {
            color: #e17055;
        }

        .news-title {
            font-size: 20px;
            margin-bottom: 10px;
            color: #333;
        }

        .news-content {
            color: #666;
            line-height: 1.5;
        }

        /* Подвал */
        .footer {
            text-align: center;
            margin-top: 30px;
            padding: 20px;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>off<span>cide</span> news</h1>
            <p style="margin-top: 10px;">Футбол • Хоккей</p>
        </div>

        <div class="filter">
            <button class="filter-btn active" onclick="filterNews('all')">Все</button>
            <button class="filter-btn" onclick="filterNews('Футбол')">⚽ Футбол</button>
            <button class="filter-btn" onclick="filterNews('Хоккей')">🏒 Хоккей</button>
        </div>

        <div class="news-list" id="newsList">
            {% for news in news_list %}
            <div class="news-item {{ news.category.lower() }}" data-category="{{ news.category }}">
                <div class="news-header">
                    <span class="news-category {{ news.category.lower() }}">{{ news.category }}</span>
                    <span>{{ news.date }}</span>
                </div>
                <h3 class="news-title">{{ news.title }}</h3>
                <p class="news-content">{{ news.content }}</p>
            </div>
            {% endfor %}
        </div>

        <div class="footer">
            <p>© 2025 Offcide News</p>
        </div>
    </div>

    <script>
        function filterNews(category) {
            const items = document.querySelectorAll('.news-item');
            const buttons = document.querySelectorAll('.filter-btn');

            // Обновляем кнопки
            buttons.forEach(btn => {
                btn.classList.remove('active');
                if (btn.textContent.includes(category) || (category === 'all' && btn.textContent === 'Все')) {
                    btn.classList.add('active');
                }
            });

            // Фильтруем новости
            items.forEach(item => {
                if (category === 'all' || item.dataset.category === category) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        }
    </script>
</body>
</html>
'''


@app.route('/')
def index():
    return render_template_string(TEMPLATE, news_list=news_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)