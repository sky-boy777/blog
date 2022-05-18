from haystack import indexes
from apps.movie_app.models import MovieModel  # 导入模型类


class MovieModelIndex(indexes.SearchIndex, indexes.Indexable):
    """指定对某个模型类的哪些数据建立索引"""
    # 索引字段，use_template指定根据表中哪些字段建立索引文件，说明放在一个文件中
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        """实现抽象方法"""
        # 返回模型类
        return MovieModel

    def index_queryset(self, using=None):
        """实现抽象方法，建立索引的数据"""
        return self.get_model().objects.all()