# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..minc import Extract


def test_Extract_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    count=dict(argstr='-count %s',
    sep=',',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    flip_any_direction=dict(argstr='-any_direction',
    xor=(u'flip_positive_direction', u'flip_negative_direction', u'flip_any_direction'),
    ),
    flip_negative_direction=dict(argstr='-negative_direction',
    xor=(u'flip_positive_direction', u'flip_negative_direction', u'flip_any_direction'),
    ),
    flip_positive_direction=dict(argstr='-positive_direction',
    xor=(u'flip_positive_direction', u'flip_negative_direction', u'flip_any_direction'),
    ),
    flip_x_any=dict(argstr='-xanydirection',
    xor=(u'flip_x_positive', u'flip_x_negative', u'flip_x_any'),
    ),
    flip_x_negative=dict(argstr='-xdirection',
    xor=(u'flip_x_positive', u'flip_x_negative', u'flip_x_any'),
    ),
    flip_x_positive=dict(argstr='+xdirection',
    xor=(u'flip_x_positive', u'flip_x_negative', u'flip_x_any'),
    ),
    flip_y_any=dict(argstr='-yanydirection',
    xor=(u'flip_y_positive', u'flip_y_negative', u'flip_y_any'),
    ),
    flip_y_negative=dict(argstr='-ydirection',
    xor=(u'flip_y_positive', u'flip_y_negative', u'flip_y_any'),
    ),
    flip_y_positive=dict(argstr='+ydirection',
    xor=(u'flip_y_positive', u'flip_y_negative', u'flip_y_any'),
    ),
    flip_z_any=dict(argstr='-zanydirection',
    xor=(u'flip_z_positive', u'flip_z_negative', u'flip_z_any'),
    ),
    flip_z_negative=dict(argstr='-zdirection',
    xor=(u'flip_z_positive', u'flip_z_negative', u'flip_z_any'),
    ),
    flip_z_positive=dict(argstr='+zdirection',
    xor=(u'flip_z_positive', u'flip_z_negative', u'flip_z_any'),
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    image_maximum=dict(argstr='-image_maximum %s',
    ),
    image_minimum=dict(argstr='-image_minimum %s',
    ),
    image_range=dict(argstr='-image_range %s %s',
    ),
    input_file=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    nonormalize=dict(argstr='-nonormalize',
    xor=(u'normalize', u'nonormalize'),
    ),
    normalize=dict(argstr='-normalize',
    xor=(u'normalize', u'nonormalize'),
    ),
    out_file=dict(argstr='> %s',
    genfile=True,
    position=-1,
    ),
    output_file=dict(hash_files=False,
    keep_extension=False,
    name_source=[u'input_file'],
    name_template='%s.raw',
    position=-1,
    ),
    start=dict(argstr='-start %s',
    sep=',',
    ),
    terminal_output=dict(nohash=True,
    ),
    write_ascii=dict(argstr='-ascii',
    xor=(u'write_ascii', u'write_ascii', u'write_byte', u'write_short', u'write_int', u'write_long', u'write_float', u'write_double', u'write_signed', u'write_unsigned'),
    ),
    write_byte=dict(argstr='-byte',
    xor=(u'write_ascii', u'write_ascii', u'write_byte', u'write_short', u'write_int', u'write_long', u'write_float', u'write_double', u'write_signed', u'write_unsigned'),
    ),
    write_double=dict(argstr='-double',
    xor=(u'write_ascii', u'write_ascii', u'write_byte', u'write_short', u'write_int', u'write_long', u'write_float', u'write_double', u'write_signed', u'write_unsigned'),
    ),
    write_float=dict(argstr='-float',
    xor=(u'write_ascii', u'write_ascii', u'write_byte', u'write_short', u'write_int', u'write_long', u'write_float', u'write_double', u'write_signed', u'write_unsigned'),
    ),
    write_int=dict(argstr='-int',
    xor=(u'write_ascii', u'write_ascii', u'write_byte', u'write_short', u'write_int', u'write_long', u'write_float', u'write_double', u'write_signed', u'write_unsigned'),
    ),
    write_long=dict(argstr='-long',
    xor=(u'write_ascii', u'write_ascii', u'write_byte', u'write_short', u'write_int', u'write_long', u'write_float', u'write_double', u'write_signed', u'write_unsigned'),
    ),
    write_range=dict(argstr='-range %s %s',
    ),
    write_short=dict(argstr='-short',
    xor=(u'write_ascii', u'write_ascii', u'write_byte', u'write_short', u'write_int', u'write_long', u'write_float', u'write_double', u'write_signed', u'write_unsigned'),
    ),
    write_signed=dict(argstr='-signed',
    xor=(u'write_signed', u'write_unsigned'),
    ),
    write_unsigned=dict(argstr='-unsigned',
    xor=(u'write_signed', u'write_unsigned'),
    ),
    )
    inputs = Extract.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Extract_outputs():
    output_map = dict(output_file=dict(),
    )
    outputs = Extract.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
