import arcpy
import os
import config


def get_m_number_list(m_number_source_fc):
    print("Getting M number list")
    m_number_list = []
    with arcpy.da.SearchCursor(m_number_source_fc, ['area_name']) as cursor:
        for row in cursor:
            m_number_list.append(row[0])
    m_number_set = set(m_number_list)
    m_number_list = list(m_number_set)
    return m_number_list


def get_zinger_area_dict(m_number_list, zingers, areas):
    print("Creating zinger/ area dictionary")
    m_num_dict = {}

    for number in m_number_list:
        print(number)

        zinger = select_and_copy_m_records(zingers, number, "zinger")
        area = select_and_copy_m_records(areas, number, "area")

        m_num_dict[zinger] = area
        del zinger
        del area
        print(len(m_num_dict))
    return m_num_dict


def erase_zingers_by_areas(m_num_dict):
    print("Erasing zingers and creating result list")
    erase_list = []

    for zinger, area in m_num_dict.items():
        zinger_name = os.path.basename(str(zinger))
        print(zinger_name)
        erase_zinger = arcpy.Erase_analysis(zinger, area, r"in_memory\erase_{}".format(zinger_name))
        erase_list.append(erase_zinger)
        del erase_zinger
        print(len(erase_list))
    return erase_list


def create_erased_zingers(zingers_source, areas_source):
    fc_name = get_copy_basename(zingers_source) + "_erase"
    print("Creating erased zingers for {}".format(fc_name))
    m_number_list = get_m_number_list(zingers_source)
    zinger_area_dict = get_zinger_area_dict(m_number_list, zingers_source, areas_source)
    erase_list = erase_zingers_by_areas(zinger_area_dict)
    print(str(erase_list))
    full_output_name = os.path.join(config.output_gdb, fc_name)
    print(str(full_output_name))
    print("Merging erase results")
    arcpy.Merge_management(erase_list, full_output_name)
    print("Writing output to{}".format(full_output_name))


def select_and_copy_m_records(input, number, type): #type = eg 'zinger' or 'area'
    fl = arcpy.MakeFeatureLayer_management(input, r"in_memory\{}fl{}".format(type, number), "area_name = '{}'".format(number))
    result = arcpy.CopyFeatures_management(fl, r"in_memory\{}copy{}".format(type, number))
    return result


def get_copy_basename(copy_object):
    basename = os.path.basename(str(copy_object))
    basename_split = basename.split('_')[0]
    return basename_split