from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$',                                       'strains.views.index'),
                       url(r'^load_references/$',                       'strains.views.load_references'),
                       url(r'^save_references/$',                       'strains.views.save_references'),
                       url(r'^references/$',                            'strains.views.references'),
                       url(r'^(?P<strain_id>\d+)/$',                    'strains.views.detail'),
                       url(r'^(?P<strain_id>\d+)/contigs/$',            'strains.views.contigs'),
                       url(r'^new_strain/$',                            'strains.views.new_strain'),
                       url(r'^save_new_strain/$',                       'strains.views.save_new_strain'),
                       url(r'^add_contigs/(?P<strain_id>\d+)/$',        'strains.views.add_contigs'),
                       url(r'^save_contigs/(?P<strain_id>\d+)/$',       'strains.views.save_contigs'),
                       url(r'^contig_detail/(?P<contig_id>\d+)/$',      'strains.views.contig_detail'),
                       url(r'^add_features/(?P<strain_id>\d+)/$',       'strains.views.add_features'),
                       url(r'^save_features/(?P<strain_id>\d+)/$',      'strains.views.save_features'),
                       url(r'^features_by_contig/(?P<contig_id>\d+)/$', 'strains.views.features_by_contig'),
                       url(r'^(?P<strain_id>\d+)/features_by_strain/$', 'strains.views.features_by_strain'),
                       url(r'^(?P<strain_id>\d+)/add_CDS/$',            'strains.views.add_CDS'),
                       url(r'^(?P<strain_id>\d+)/add_protein/$',        'strains.views.add_protein'),
                       url(r'^(?P<strain_id>\d+)/save_CDS/$',           'strains.views.save_CDS'),
                       url(r'^(?P<strain_id>\d+)/save_protein/$',       'strains.views.save_protein'),
                       url(r'^feature_detail/(?P<feature_id>\d+)/$',    'strains.views.feature_detail'),
                       url(r'^gene_detail/(?P<reference_id>\d+)/$',     'strains.views.gene_detail'),
                       url(r'^cds_clustal/(?P<reference_id>\d+)/$',     'strains.views.cds_clustal'),
                       url(r'^protein_clustal/(?P<reference_id>\d+)/$', 'strains.views.protein_clustal'),
                       url(r'^(?P<strain_id>\d+)/strain_cds/$',         'strains.views.strain_cds'),
                       url(r'^(?P<strain_id>\d+)/strain_protein/$',     'strains.views.strain_protein'),
                       url(r'^(?P<strain_id>\d+)/strain_contigs/$',     'strains.views.strain_contigs'),
                       url(r'^(?P<strain_id>\d+)/delete_strain/$',      'strains.views.delete_strain'),
                      )
