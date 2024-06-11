from sqlglot import parse_one, exp


class SQLParser:
    
    _SCALAR_KEYWORDS = (exp.Abs, exp.Length, exp.Cast, exp.Round, exp.Upper, exp.Lower, exp.Rand)
    _SCALAR_KEYWORDS_ANONYMOUS_STR = ("STRFTIME", "JULIADAY", "NOW", "INSTR", "SUBSTR")
    
    _MATH_COMPUTE_KEYWORDS = (exp.Add, exp.Sub, exp.Mul, exp.Div, exp.Mod)
    
    def __init__(self, sql, dialect="sqlite"):
        self.ast = parse_one(sql, dialect=dialect)
    
    @property
    def count_table(self):
        return len(list(self.ast.find_all(exp.Table)))
    
    @property
    def count_select(self):
        return len(list(self.ast.find_all(exp.Select)))

    @property
    def count_aggregation(self):
        return len(list(self.ast.find_all(exp.AggFunc)))
    
    @property
    def count_scalar_function(self):
        scalar_nodes = list(self.ast.find_all(self._SCALAR_KEYWORDS))
        scalar_nodes.extend([node for node in self.ast.find_all(exp.Anonymous) if node.this.upper() in self._SCALAR_KEYWORDS_ANONYMOUS_STR])
        return len(scalar_nodes)

    @property
    def count_math_compute(self):
        return len(list(self.ast.find_all(self._MATH_COMPUTE_KEYWORDS)))
