%define oname	Qemulator

Summary:	Interface to configure and launch Qemu
Name:		qemulator
Version:	0.5
Release:	%mkrel 9
License:	GPLv2+
Group:		Emulators
URL:		http://qemulator.createweb.de/
Source0:	http://qemulator.createweb.de/%{oname}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		fix_python_dir.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

Requires:	perl-Locale-gettext >= 1.04
Requires:	python
Requires:	pygtk2.0
Requires:	gnome-python
Requires:	qemu
Requires:	pygtk2.0-libglade
BuildRequires:	librsvg
BuildRequires:	libxml2-utils
BuildRequires:	desktop-file-utils
BuildRequires:	libglade2.0-devel
BuildRequires:	pygtk2.0-devel
BuildRequires:	imagemagick

%description
A launcher for Qemu that manages Qemu configs and creates disk images
Qemu-launcher provides a point and click interface to Qemu. It also
allows you to create, save, load, and run multiple Qemu VM
configurations. It has a basic interface for creating or converting
disk images.

Only supports the x86 PC emulator part of Qemu.


%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir} \
         %{buildroot}%{_datadir}/ \
         %{buildroot}%{_datadir}/%{name} \
         %{buildroot}%{_datadir}/pixmaps \
         %{buildroot}%{_libdir}
cp -a usr/local/lib/qemulator/* %{buildroot}%{_datadir}/qemulator
cp -ra usr/local/share/* %{buildroot}%{_datadir}/
chmod +x %{buildroot}%{_datadir}/qemulator/qml_imagecreation.py \
         %{buildroot}%{_datadir}/qemulator/qml_machinesetup.py \
         %{buildroot}%{_datadir}/qemulator/qml_filehandlers.py \
         %{buildroot}%{_datadir}/qemulator/qml_configuration.py \
         %{buildroot}%{_datadir}/qemulator/qml_tools.py \
         %{buildroot}%{_datadir}/qemulator/qml_installwizzard.py \
         %{buildroot}%{_datadir}/qemulator/qml_style.py
chmod -x %{buildroot}%{_datadir}/qemulator/icons/mac.png
convert -resize 32x32 usr/local/share/pixmaps/qemulator.svg qemulator.xpm
cp qemulator.xpm %{buildroot}%{_datadir}/pixmaps/
ln -s %{_datadir}/qemulator/qemulator.py %{buildroot}%{_bindir}/qemulator

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/pixmaps/%{name}/%{name}.*
%{_datadir}/locale
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/pixmaps/qemulator/*.png
