import numpy as np
from IPython.display import IFrame, Markdown, Latex, display

def _get_kwargs(name, default, **kwargs):
    ret = default
    if name in kwargs:
        ret = kwargs.get(name)
    return ret

def _bool_to_str(boolean):
    return str(boolean).lower()

def display_geogebra(id, **kwargs):
    """
        Displays a geogebra interactive applet as a Jupyter Notebook cell.
    """
    width          = _get_kwargs('width', 800, **kwargs)
    height         = _get_kwargs('height', 600, **kwargs)
    fullscreen_btn = _bool_to_str(_get_kwargs('fullscreen', True, **kwargs))
    menu_bar       = _bool_to_str(_get_kwargs('menu_bar', False, **kwargs))
    top_bar        = _bool_to_str(_get_kwargs('top_bar', False, **kwargs))
    grid_options   = _bool_to_str(_get_kwargs('grid_options', False, **kwargs))
    reset_button   = _bool_to_str(_get_kwargs('reset_button', True, **kwargs))
    pan_and_zoom   = _bool_to_str(_get_kwargs('pan_and_zoom', True, **kwargs))
    paused = _bool_to_str(_get_kwargs('paused', False, **kwargs))

    src_str = f'https://www.geogebra.org/material/iframe/id/{id}/width/{width}/height/{height}/border/888888/sfsb/{fullscreen_btn}/smb/{menu_bar}/stb/{top_bar}/stbh/true/ai/false/asb/{grid_options}/sri/{reset_button}/rc/false/ld/false/sdz/{pan_and_zoom}/ctl/{paused}'
    display(IFrame(src=src_str, width=width, height=height))

def display_matrix(m):
    display(Latex(matrix_to_latex(m)))

def matrix_to_latex(m):
    tp = type(m)
    if tp != np.ndarray and tp != list:
        raise TypeError('m must be of type np.array or list')

    if len(m.shape) == 1:
        m = m.reshape(1, m.shape[0]) 

    str_and = '& '
    str_cr  = '\\\\ '

    ltx_list = ''.join([ 
        ''.join([f'{m[i, j]} { str_and if j < m.shape[1]-1 else str_cr }' for j in range(m.shape[1])])
        for i in range(m.shape[0])
    ])
    ltx_str  = f'\\begin{{bmatrix}}\n{ltx_list}\\end{{bmatrix}}'

    return ltx_str

if __name__ == '__main__':
    arr = np.array([[1.2, 2, 3], [3, 2, 1]])
    print(matrix_to_latex(arr))
    
