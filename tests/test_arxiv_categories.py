"""
THIS FILE IS AUTOGENERATED.
DO NOT MODIFY.
INSTEAD, RUN scripts/scrape_categories.py
"""

import unittest

from pyarxiv.arxiv_categories import *


class TestArxivCategories(unittest.TestCase):
    def test_categories(self):
        self.assertEqual(
            arxiv_category_map[ArxivCategory.stat_AP],
            'stat.AP')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.stat_CO],
            'stat.CO')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.stat_ML],
            'stat.ML')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.stat_ME],
            'stat.ME')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.stat_TH],
            'stat.TH')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.q_bio_BM],
            'q-bio.BM')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.q_bio_CB],
            'q-bio.CB')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.q_bio_GN],
            'q-bio.GN')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.q_bio_MN],
            'q-bio.MN')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.q_bio_NC],
            'q-bio.NC')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.q_bio_OT],
            'q-bio.OT')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.q_bio_PE],
            'q-bio.PE')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.q_bio_QM],
            'q-bio.QM')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.q_bio_SC],
            'q-bio.SC')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.q_bio_TO],
            'q-bio.TO')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_AR],
            'cs.AR')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_AI],
            'cs.AI')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_CL],
            'cs.CL')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_CC],
            'cs.CC')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_CE],
            'cs.CE')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_CG],
            'cs.CG')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_GT],
            'cs.GT')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_CV],
            'cs.CV')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_CY],
            'cs.CY')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_CR],
            'cs.CR')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_DS],
            'cs.DS')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_DB],
            'cs.DB')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_DL],
            'cs.DL')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_DM],
            'cs.DM')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_DC],
            'cs.DC')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_GL],
            'cs.GL')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_GR],
            'cs.GR')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_HC],
            'cs.HC')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_IR],
            'cs.IR')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_IT],
            'cs.IT')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_LG],
            'cs.LG')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_LO],
            'cs.LO')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_MS],
            'cs.MS')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_MA],
            'cs.MA')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_MM],
            'cs.MM')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_NI],
            'cs.NI')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_NE],
            'cs.NE')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_NA],
            'cs.NA')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_OS],
            'cs.OS')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_OH],
            'cs.OH')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_PF],
            'cs.PF')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_PL],
            'cs.PL')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_RO],
            'cs.RO')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_SE],
            'cs.SE')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_SD],
            'cs.SD')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cs_SC],
            'cs.SC')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.nlin_AO],
            'nlin.AO')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.nlin_CG],
            'nlin.CG')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.nlin_CD],
            'nlin.CD')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.nlin_SI],
            'nlin.SI')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.nlin_PS],
            'nlin.PS')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_AG],
            'math.AG')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_AT],
            'math.AT')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_AP],
            'math.AP')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_CT],
            'math.CT')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_CA],
            'math.CA')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_CO],
            'math.CO')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_AC],
            'math.AC')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_CV],
            'math.CV')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_DG],
            'math.DG')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_DS],
            'math.DS')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_FA],
            'math.FA')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_GM],
            'math.GM')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_GN],
            'math.GN')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_GT],
            'math.GT')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_GR],
            'math.GR')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_HO],
            'math.HO')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_IT],
            'math.IT')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_KT],
            'math.KT')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_LO],
            'math.LO')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_MP],
            'math.MP')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_MG],
            'math.MG')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_NT],
            'math.NT')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_NA],
            'math.NA')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_OA],
            'math.OA')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_OC],
            'math.OC')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_PR],
            'math.PR')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_QA],
            'math.QA')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_RT],
            'math.RT')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_RA],
            'math.RA')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_SP],
            'math.SP')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_ST],
            'math.ST')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_SG],
            'math.SG')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.astro_ph],
            'astro-ph')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cond_mat_dis_nn],
            'cond-mat.dis-nn')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cond_mat_mes_hall],
            'cond-mat.mes-hall')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cond_mat_mtrl_sci],
            'cond-mat.mtrl-sci')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cond_mat_other],
            'cond-mat.other')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cond_mat_soft],
            'cond-mat.soft')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cond_mat_stat_mech],
            'cond-mat.stat-mech')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cond_mat_str_el],
            'cond-mat.str-el')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.cond_mat_supr_con],
            'cond-mat.supr-con')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.gr_qc],
            'gr-qc')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.hep_ex],
            'hep-ex')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.hep_lat],
            'hep-lat')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.hep_ph],
            'hep-ph')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.hep_th],
            'hep-th')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.math_ph],
            'math-ph')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.nucl_ex],
            'nucl-ex')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.nucl_th],
            'nucl-th')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.physics_acc_ph],
            'physics.acc-ph')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.physics_ao_ph],
            'physics.ao-ph')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.physics_atom_ph],
            'physics.atom-ph')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.physics_atm_clus],
            'physics.atm-clus')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.physics_bio_ph],
            'physics.bio-ph')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.physics_chem_ph],
            'physics.chem-ph')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.physics_class_ph],
            'physics.class-ph')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.physics_comp_ph],
            'physics.comp-ph')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.physics_data_an],
            'physics.data-an')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.physics_flu_dyn],
            'physics.flu-dyn')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.physics_gen_ph],
            'physics.gen-ph')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.physics_geo_ph],
            'physics.geo-ph')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.physics_hist_ph],
            'physics.hist-ph')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.physics_ins_det],
            'physics.ins-det')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.physics_med_ph],
            'physics.med-ph')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.physics_optics],
            'physics.optics')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.physics_ed_ph],
            'physics.ed-ph')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.physics_soc_ph],
            'physics.soc-ph')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.physics_plasm_ph],
            'physics.plasm-ph')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.physics_pop_ph],
            'physics.pop-ph')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.physics_space_ph],
            'physics.space-ph')
        self.assertEqual(
            arxiv_category_map[ArxivCategory.quant_ph],
            'quant-ph')

if __name__ == "__main__":
    unittest.main()