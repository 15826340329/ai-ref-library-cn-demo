import json

ASSETS = [
    {'id': 1, 'name': '自然微笑脸', 'category': '脸', 'tags': ['自然', '微笑', '女性']},
    {'id': 2, 'name': '商务站姿', 'category': '姿势', 'tags': ['商务', '站姿', '男性']},
    {'id': 3, 'name': '街头风外套', 'category': '服装', 'tags': ['街头', '外套', '潮流']},
    {'id': 4, 'name': '侧脸特写', 'category': '脸', 'tags': ['侧脸', '特写', '中性']},
    {'id': 5, 'name': '坐姿阅读', 'category': '姿势', 'tags': ['坐姿', '阅读', '安静']},
]


def search(query: str, category: str | None = None):
    q = query.lower().strip()
    results = []
    for asset in ASSETS:
        if category and asset['category'] != category:
            continue
        text = ' '.join([asset['name'], asset['category'], *asset['tags']]).lower()
        if q in text:
            results.append(asset)
    return results


def show(results):
    if not results:
        print('没有找到匹配素材。')
        return
    print(f'找到 {len(results)} 个素材：')
    for item in results:
        tags = ', '.join(item['tags'])
        print(f"- #{item['id']} {item['name']} | 分类: {item['category']} | 标签: {tags}")


def main():
    print('AI 作图素材库 · 中文版 Demo')
    print('分类：脸 / 姿势 / 服装')
    query = input('输入关键词（如 微笑 / 商务 / 街头）：').strip()
    category = input('输入分类（回车跳过）：').strip() or None
    if category and category not in ['脸', '姿势', '服装']:
        print('分类不存在，将忽略分类筛选。')
        category = None
    show(search(query, category))


if __name__ == '__main__':
    main()