acura=['ilx', 'mdx', 'nsx', 'rdx', 'rlx', 'tlx', 'cl', 'ilx-hybrid', 'integra', 'legend', 'rl', 'rsx', 'slx', 'tl', 'tsx', 'tsx-sport-wagon', 'vigor', 'zdx']
hyundai=['accent', 'azera', 'elantra', 'elantra-gt', 'ioniq-electric', 'ioniq-hybrid', 'ioniq-plug-in-hybrid', 'kona', 'kona-electric', 'nexo', 'palisade', 'santa-fe', 'santa-fe-sport', 'santa-fe-xl', 'sonata', 'sonata-hybrid', 'sonata-plug-in-hybrid', 'tucson', 'veloster', 'venue', 'elantra-coupe', 'elantra-touring', 'entourage', 'equus', 'excel', 'genesis', 'genesis-coupe', 'scoupe', 'tiburon', 'veracruz', 'xg300', 'xg350']
kia=['cadenza', 'forte', 'k900', 'niro', 'niro-ev', 'niro-plug-in-hybrid', 'optima', 'optima-hybrid', 'optima-plug-in-hybrid', 'rio', 'sedona', 'seltos', 'sorento', 'soul', 'soul-ev', 'sportage', 'stinger', 'telluride', 'amanti', 'borrego', 'rondo', 'sephia', 'spectra']
mazda=['3', '6', 'cx-3', 'cx-30', 'cx-5', 'cx-9', 'mx-5-miata', 'mx-5-miata-rf', '2', '323', '5', '626', '929', 'b-series', 'b-series-pickup', 'b-series-truck', 'cx-7', 'mazdaspeed-3', 'mazdaspeed-6', 'mazdaspeed-mx-5-miata', 'mazdaspeed-protege', 'millenia', 'mpv', 'mx-3', 'mx-6', 'navajo', 'protege', 'protege5', 'rx-7', 'rx-8', 'tribute', 'tribute-hybrid', 'truck']
nissan=['370z', 'altima', 'armada', 'frontier', 'gt-r', 'kicks', 'leaf', 'maxima', 'murano', 'nv-cargo', 'nv-passenger', 'nv200', 'pathfinder', 'rogue', 'rogue-sport', 'sentra', 'titan', 'titan-xd', 'versa', 'versa-note', '200sx', '240sx', '300zx', '350z', 'altima-hybrid', 'axxess', 'cube', 'juke', 'murano-crosscabriolet', 'nv', 'nx', 'pulsar', 'quest', 'rogue-select', 'stanza', 'truck', 'van', 'xterra']
mitsubishi=['eclipse-cross', 'mirage', 'mirage-g4', 'outlander', 'outlander-phev', 'outlander-sport', '3000gt', 'diamante', 'eclipse', 'eclipse-spyder', 'endeavor', 'expo', 'galant', 'i-miev', 'lancer', 'lancer-evolution', 'lancer-sportback', 'mighty-max-pickup', 'montero', 'montero-sport', 'precis', 'raider', 'sigma', 'vanwagon']
volvo=['s60', 's60-cross-country', 's90', 'v60', 'v60-cross-country', 'v90', 'v90-cross-country', 'xc40', 'xc60', 'xc90', '240', '740', '760', '780', '850', '940', '960', 'c30', 'c70', 'coupe', 's40', 's70', 's80', 'v40', 'v50', 'v70', 'xc', 'xc70']
suzuki=['select-model', 'aerio', 'equator', 'esteem', 'forenza', 'grand-vitara', 'kizashi', 'reno', 'samurai', 'sidekick', 'swift', 'sx4', 'verona', 'vitara', 'x-90', 'xl-7', 'xl7', 'select-model', 'aerio', 'equator', 'esteem', 'forenza', 'grand-vitara', 'kizashi', 'reno', 'samurai', 'sidekick', 'swift', 'sx4', 'verona', 'vitara', 'x-90', 'xl-7', 'xl7', 'select-model', 'aerio', 'equator', 'esteem', 'forenza', 'grand-vitara', 'kizashi', 'reno', 'samurai', 'sidekick', 'swift', 'sx4', 'verona', 'vitara', 'x-90', 'xl-7', 'xl7']

#'coupe','wagon','sedan','hatchback','suv','type-s','32-type-s','hybrid','type-r'}
car_year=[
       '2000','2001'
       ]

companies=['acura','hyundai','kia','mazda','nissan','mitsubishi','volvo','suzuki']
for com in companies:
    for mod in eval(com):
        print(mod)
        
